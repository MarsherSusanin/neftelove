from flask import Flask, request, jsonify, Response, redirect, flash, make_response
from flask import render_template, url_for
from flask_cors import CORS, cross_origin

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import sentinelhub
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox, DataCollection, bbox_to_dimensions, geo_utils

import matplotlib.pyplot as plt
from matplotlib import cm

import io
import base64
from base64 import encodebytes
import os
import PIL.Image as Image
import numpy as np
from numpyencoder import NumpyEncoder
import pandas as pd
import math
import cv2

from scipy.signal import argrelextrema, resample
from scipy import interpolate

import json

from pyproj import Proj, transform
# Убираем warning бтблиотеки pyproj:
import warnings
warnings.filterwarnings('ignore')

app_dir = os.path.abspath(os.path.dirname(__file__))

flask_app = Flask(__name__)
flask_app.secret_key = 'secret'

# пришлось добавить эту штуку чтобы решить проблему с blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
CORS(flask_app)

def download_data(data):
    name_sputnik = data["name_sputnik"]
    maxcc = int(data["maxcc"]) #20
    time_interval = data["time_interval"] #'2021-08-08/2021-08-10'
    # Координаты нижнего левого угла
    lat = float(data["lat"]) #44.469596
    long = float(data["long"]) #37.133366
    iLeng = int(data["iLeng"])*1000 #100*1000 # в метрах

    # Пересчитываем широту и долготу в метры:
    xTopLeft, yTopLeft = transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), long, lat) # Долгота первая, широта вторая
    xDownRight = xTopLeft + iLeng
    yDownRight = yTopLeft + iLeng
    s = f'{xTopLeft:.6f},{yTopLeft:.6f},{xDownRight:.6f},{yDownRight:.6f}'

    #print("Регистрация на сайте sentinel-hub")
    # Регистрация на сайте sentinel-hub:
    # Your client credentials
    client_id = '7efeab3b-7078-49be-9066-8103ab134190'
    client_secret = '-[r>N!h>]WAW*/p*UF?z.^YIc(+cM_3f|fd>OBj]'
    # Create a session
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    # Get token for the session
    token = oauth.fetch_token(token_url='https://services.sentinel-hub.com/oauth/token',client_secret=client_secret)

    # Скачиваем данные снимков:
    if name_sputnik == 'sentinel-1':
        print('Запрашиваем VV картинку...')
        resp = oauth.get("https://services.sentinel-hub.com/ogc/wms/d0cd7109-da26-401b-add9-cc26a4ab2982?REQUEST=GetMap&BBOX="+s+"&LAYERS=IW_VV&MAXCC="+str(maxcc)+"&WIDTH=1000&HEIGHT=1000&FORMAT=image/jpeg&TIME="+time_interval)
        imgVV = Image.open(io.BytesIO(resp.content))
        BVV = np.asarray(imgVV)
        #imgVV.save('VV.jpg')
        print('VV картинка получена!')
        print('Запрашиваем VH картинку...')
        resp = oauth.get("https://services.sentinel-hub.com/ogc/wms/d0cd7109-da26-401b-add9-cc26a4ab2982?REQUEST=GetMap&BBOX="+s+"&LAYERS=IW_VH&MAXCC="+str(maxcc)+"&WIDTH=1000&HEIGHT=1000&FORMAT=image/jpeg&TIME="+time_interval)
        imgVH = Image.open(io.BytesIO(resp.content))
        BVH = np.asarray(imgVH)
        #imgVH.save('VH.jpg')
        print('VH картинка получена!')
        return BVV, BVH
    elif name_sputnik == 'sentinel-2':
        print('Запрашиваем картинку B02...')
        resp = oauth.get("https://services.sentinel-hub.com/ogc/wms/88cab0ae-fe80-4864-af65-3ad7bd015d17?REQUEST=GetMap&BBOX="+s+"&LAYERS=SB02&MAXCC="+str(maxcc)+"&WIDTH=1000&HEIGHT=1000&FORMAT=image/jpeg&TIME="+time_interval)
        imgB02 = Image.open(io.BytesIO(resp.content))
        B02 = np.asarray(imgB02)
        #imgB02.save('B02.jpg')
        print('B02 картинка получена!')
        print('Запрашиваем картинку B03...')
        resp = oauth.get("https://services.sentinel-hub.com/ogc/wms/88cab0ae-fe80-4864-af65-3ad7bd015d17?REQUEST=GetMap&BBOX="+s+"&LAYERS=SB03&MAXCC="+str(maxcc)+"&WIDTH=1000&HEIGHT=1000&FORMAT=image/jpeg&TIME="+time_interval)
        imgB03 = Image.open(io.BytesIO(resp.content))
        B03 = np.asarray(imgB03)
        #imgB03.save('B03.jpg')
        print('B03 картинка получена!')
        print('Запрашиваем картинку B04...')
        resp = oauth.get("https://services.sentinel-hub.com/ogc/wms/88cab0ae-fe80-4864-af65-3ad7bd015d17?REQUEST=GetMap&BBOX="+s+"&LAYERS=SB04&MAXCC="+str(maxcc)+"&WIDTH=1000&HEIGHT=1000&FORMAT=image/jpeg&TIME="+time_interval)
        imgB04 = Image.open(io.BytesIO(resp.content))
        B04 = np.asarray(imgB04)
        #imgB04.save('B04.jpg')
        print('B04 картинка получена!')
        return B02, B03, B04

def stretch(val, min1, max1):
    return (val - min1) / (max1 - min1)

def analysis_color_pixel_2(pixel,BVV,BVH):
    if BVH == 0:
        BVH = 1
    if (BVV/BVH) > 8:
        n = 4
        m1 = 25
        # Рассчитываем значение фильтра Баттерворта для значения массива VV:
        butt1 = 1-1/(1+math.pow(-1,n)*math.pow((BVV/(m1/2)),2*n))
        if butt1 > 0.1:
            pixel = 255 * math.pow(butt1,0)
        else:
            pixel = stretch(BVV*math.pow(butt1,3),0.10*255,0.30*255)
    else:
        n = 4
        m1 = 5
        # Рассчитываем значение фильтра Баттерворта для значения массива VV:
        buttV = 1-1/(1+math.pow(-1,n)*math.pow((BVV/(m1/2)),2*n))
        # Рассчитываем значение фильтра Баттерворта для значения массива VH:
        buttH = 1-1/(1+math.pow(-1,n)*math.pow((BVH/(m1/2)),2*n))
        pixel = BVH * buttH * 8
    return pixel

def analysis_color_pixel_1(pixel,BVV,BVH):
    if BVH == 0:
        BVH = 1
    if (BVV/BVH) > 8:
        n = 4
        m1 = 25
        # Рассчитываем значение фильтра Баттерворта для значения массива VV:
        butt1 = 1-1/(1+math.pow(-1,n)*math.pow((BVV/(m1/2)),2*n))
        if butt1 > 0.1:
            pixel = 255 * math.pow(butt1,0)
        else:
            pixel = stretch(BVV*math.pow(butt1,3),0.10*255,0.30*255)
    else:
        n = 4
        m1 = 5
        # Рассчитываем значение фильтра Баттерворта для значения массива VV:
        buttV = 1-1/(1+math.pow(-1,n)*math.pow((BVV/(m1/2)),2*n))
        # Рассчитываем значение фильтра Баттерворта для значения массива VH:
        buttH = 1-1/(1+math.pow(-1,n)*math.pow((BVH/(m1/2)),2*n))
        pixel = BVV * buttV * 10 + BVH * buttH * 15
    return pixel

def analysis_color_pixel_0(pixel,BVV,BVH):
    #print(BVH)
    if BVH == 0:
        BVH = 1
    if (BVV/BVH) > 8:
        n = 4
        m1 = 25
        # Рассчитываем значение фильтра Баттерворта для значения массива VV:
        butt1 = 1-1/(1+math.pow(-1,n)*math.pow((BVV/(m1/2)),2*n))
        if butt1 > 0.1:
            pixel = 255
        else:
            pixel = stretch(BVV*math.pow(butt1,3),0.20*255,0.99*255)
    else:
        n = 4
        m1 = 5
        # Рассчитываем значение фильтра Баттерворта для значения массива VV:
        buttV = 1-1/(1+math.pow(-1,n)*math.pow((BVV/(m1/2)),2*n))
        # Рассчитываем значение фильтра Баттерворта для значения массива VH:
        buttH = 1-1/(1+math.pow(-1,n)*math.pow((BVH/(m1/2)),2*n))
        pixel = 0
    return pixel

"""
def get_negativ_pixel(pixel):
    return 255 - pixel
"""

def analysis_data_sentinel_1(BVV,BVH,sensitivity):
    print('Start analysis Sentinel-1')
    # Создаем пустое изображение:
    # Создаем цветовую палитру по имени:
    cm2 = plt.get_cmap('gist_rainbow')
    # Применяем цветовую палитру к массиву:
    colored_image = cm2(BVV)
    # Полученную картинку с 4-мя каналами (R,G,B,A) с значениями float[0, 1] конвертируем в RGB(uint8):
    imgcc = Image.fromarray((colored_image[:, :, :3] * 255).astype(np.uint8))
    img = np.asarray(imgcc)

    # Делаем спец обработку каждого пикселя по уровню BVV/BVH:
    img[:,:,0] = np.vectorize(analysis_color_pixel_0)(img[:,:,0],BVV,BVH)
    img[:,:,1] = np.vectorize(analysis_color_pixel_1)(img[:,:,1],BVV,BVH)
    img[:,:,2] = np.vectorize(analysis_color_pixel_2)(img[:,:,2],BVV,BVH)
            
    # Размываем изображение для уничтожения мелкозернистого шума:
    # (результат - размытое изображение)
    img_blur = cv2.bilateralFilter(img, d = 40, sigmaSpace = 75, sigmaColor = 75)

    # Делаем негатив изображения
    #img_blur[:,:,0] = np.vectorize(get_negativ_pixel)(img_blur[:,:,0])
    #img_blur[:,:,1] = np.vectorize(get_negativ_pixel)(img_blur[:,:,1])
    #img_blur[:,:,2] = np.vectorize(get_negativ_pixel)(img_blur[:,:,2])
            
    # Конвертируем цветовую карту изображения в формат grayscale для того,
    #  чтобы дальше можно было применить функцию поиска контуров:
    gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    # Пропускаем изображение через пороговую функцию:
    ret, thresh = cv2.threshold(gray, sensitivity, 255, cv2.THRESH_BINARY_INV)

    # Возвращаем результрат наложения пороговой функциии:
    print('End analysis Sentinel-1')
    return thresh, img, img

def HighlightCompressVisualizer(val,minA,maxA):
    cs = (val-minA)/(maxA-minA)
    if val <= minA:
        return 0
    elif val > minA and cs <= 0.92:
        return cs
    elif val <= 0.9:
        return (0.08*(val-cs))/(0.9-cs)+0.92
    else:
        return val

def analysis_data_sentinel_2(B02, B03, B04, type_relief,sensitivity):
    print('Start analysis Sentinel-2')
    # Создаем пустое изображение:
    # Создаем цветовую палитру по имени:
    cm2 = plt.get_cmap('gist_rainbow')
    # Применяем цветовую палитру к массиву:
    colored_image = cm2(B02)
    # Полученную картинку с 4-мя каналами (R,G,B,A) с значениями float[0, 1] конвертируем в RGB(uint8):
    imgcc = Image.fromarray((colored_image[:, :, :3] * 255).astype(np.uint8))
    imgTrueColor = np.asarray(imgcc)

    # Из массивов B02, B03 и B04 делаем осветлённое TrueColor изображение:
    img = np.zeros((B02.shape[0], B02.shape[1], 3))
    img[:,:,0] = B02/50
    img[:,:,1] = B03/50
    img[:,:,2] = B04/50

    # Из массивов B02, B03 и B04 делаем обычное TrueColor изображение:
    img2 = np.zeros((B02.shape[0], B02.shape[1], 3))
    img2[:,:,0] = B02
    img2[:,:,1] = B03
    img2[:,:,2] = B04
    #cv2.imwrite('Color_(B02,B03,B04).jpg',img2)

    # Создаем массивы данных для создания HighLight-изображения:
    height, width, _ = img.shape
    minC0 = np.full((height, width), 0.2)
    maxC0 = np.full((height, width), 0.5)
    minC1 = np.full((height, width), 0.2)
    maxC1 = np.full((height, width), 0.5)
    minC2 = np.full((height, width), 0.001)
    maxC2 = np.full((height, width), 0.98)
    
    # Создаем HighLight-изображение:
    imgTrueColor[:,:,0] = np.array(np.vectorize(HighlightCompressVisualizer)(list(map(lambda x,y: x*y,B02,np.full(B02.size,4/256))),minC0,maxC0)*256,dtype=np.uint8)
    imgTrueColor[:,:,1] = np.array(np.vectorize(HighlightCompressVisualizer)(list(map(lambda x,y: x*y,B03,np.full(B03.size,4/256))),minC1,maxC1)*256,dtype=np.uint8)
    imgTrueColor[:,:,2] = np.array(np.vectorize(HighlightCompressVisualizer)(list(map(lambda x,y: x*y,B04,np.full(B04.size,2/256))),minC2,maxC2)*256,dtype=np.uint8)

    if type_relief == 1:
        # Определяем границы Фильтра диапазона красного цвета:
        # Преобразуем массив пикселей в картинку формата Jpeg:
        imgTrueColor_rgb = cv2.cvtColor(np.uint8(imgTrueColor), cv2.COLOR_BGR2RGB)
        pil_imgTrueColor = Image.fromarray(imgTrueColor_rgb)
        b = io.BytesIO()
        pil_imgTrueColor.save(b, 'jpeg')
        pil_imgTrueColor_bytes = b.getvalue()
        str_imgTrueColor = str(base64.b64encode(pil_imgTrueColor_bytes), encoding='utf-8')#.decode('utf-8')
        hightlight_image = Image.open(io.BytesIO(base64.b64decode(str_imgTrueColor)))
        img3 = np.asarray(hightlight_image)
        #img3 = cv2.cvtColor(np.uint8(img3), cv2.COLOR_BGR2RGB)
        # Строим гистограмму красного канала:
        hi0, countshi2 = np.histogram(img3[:, :, 0], range(256))#img3[:, :, 0].ravel()
        # Строим гистограмму красного канала:
        hi1, countshi1 = np.histogram(img3[:, :, 1], range(256))#hi1 = img3[:, :, 1].ravel()

        window_len = 2
        while True:
            # Сглаживаем графики гистограм:
            window_len += 1
            kernel = np.ones(window_len, dtype=float)/window_len
            smooth_hi0 = np.convolve(hi0, kernel, 'same')
            # Ищем минимумы сглаженных графиков гистограм:
            minHi0 = np.array(argrelextrema(smooth_hi0, np.less)[0])
            if minHi0.size <= 2:
                break
        if len(minHi0) < 2:
            minHi0 = np. concatenate( (minHi0, [245] ) )
        if minHi0[1] < 200:
            minHi0[1] = 245
        print(minHi0)

        window_len = 2
        while True:
            # Сглаживаем графики гистограм:
            window_len += 1
            kernel = np.ones(window_len, dtype=float)/window_len
            smooth_hi1 = np.convolve(hi1, kernel, 'same')
            # Ищем минимумы сглаженных графиков гистограм:
            minHi1 = np.array(argrelextrema(smooth_hi1, np.less)[0])
            if minHi1.size <= 5:
                break
        print(minHi1)

        # Пропускаем изображение через Фильтр диапазона красного цвета:
        hsv_min = np.array((0, 0, minHi0[0]), np.uint8) #23
        hsv_max = np.array((0, 0, minHi0[1]), np.uint8) #223
        thresh1 = cv2.inRange(imgTrueColor, hsv_min, hsv_max)

        # Пропускаем изображение через Фильтр диапазона красно-зеленого цвета:
        hsv_min = np.array((0, minHi0[0], minHi0[0]), np.uint8) #23
        hsv_max = np.array((0, minHi1[0], minHi1[0]), np.uint8) #50
        thresh2 = cv2.inRange(imgTrueColor, hsv_min, hsv_max)

        #thresh = thresh1 + thresh2

        # Размываем, чтобы убрать шум:
        #threshTrue_blur = cv2.bilateralFilter(threshTrue, d = 140, sigmaSpace = 75, sigmaColor = 75)# Convert to grayscale
        thresh1 = cv2.medianBlur(thresh1,3)
        thresh1 = cv2.medianBlur(thresh1,3)
        thresh1 = cv2.medianBlur(thresh1,3)

        thresh2 = cv2.medianBlur(thresh2,3)
        thresh2 = cv2.medianBlur(thresh2,3)
        thresh2 = cv2.medianBlur(thresh2,3)
    elif type_relief == 0:
        gray = cv2.cvtColor(imgTrueColor, cv2.COLOR_BGR2GRAY)

        # Пропускаем изображение через пороговую функцию:
        ret, thresh1 = cv2.threshold(gray, sensitivity, 255, cv2.THRESH_BINARY_INV)
        thresh2 = []
    
    # Возвращаем результрат пропуска изображения через фильтр диапазона красного цвета:
    print('End analysis Sentinel-2')
    return thresh1, thresh2, img2, imgTrueColor

@flask_app.route('/', methods=['GET', 'POST'])
def login_in():
    if request.method=='GET':
        return render_template('/home/index.html')

@flask_app.route('/getcontours', methods=['GET', 'POST'])
def get_contours():
    if request.method=='POST':
        request_data = request.get_json()
        data_dn = request_data['download_data']
        name_sputnik = request_data['name_sputnik']
        type_relief = int(request_data['type_relief'])
        sensitivity = int(request_data['sensitivity'])
        contour_line_width = int(request_data['contour_line_width'])
        #print(type_relief)
        if data_dn == 'exist':
            if name_sputnik == 'sentinel-1':
                imgVVbytes = base64.b64decode(request_data['image_VV'])
                imgVV = Image.open(io.BytesIO(imgVVbytes))
                BVV = np.asarray(imgVV)            
                imgVHbytes = base64.b64decode(request_data['image_VH'])
                imgVH = Image.open(io.BytesIO(imgVHbytes))
                BVH = np.asarray(imgVH)
            elif name_sputnik == 'sentinel-2':
                imgbytesB02 = base64.b64decode(request_data['image_B02'])
                imgB02 = Image.open(io.BytesIO(imgbytesB02))
                B02 = np.asarray(imgB02)
                imgbytesB03 = base64.b64decode(request_data['image_B03'])
                imgB03 = Image.open(io.BytesIO(imgbytesB03))
                B03 = np.asarray(imgB03)
                imgbytesB04 = base64.b64decode(request_data['image_B04'])
                imgB04 = Image.open(io.BytesIO(imgbytesB04))
                B04 = np.asarray(imgB04)
            else:
                return jsonify({"error" : "Wrong sputnik name"})
        else:
            if name_sputnik == 'sentinel-1':
                data = {}
                data["name_sputnik"] = request_data['name_sputnik']
                data["maxcc"] = request_data['maxcc']
                data["time_interval"] = request_data['time_interval']
                data["lat"] = request_data['lat']
                data["long"] = request_data['long']
                data["iLeng"] = request_data['iLeng']
                BVV, BVH = download_data(data)
            elif name_sputnik == 'sentinel-2':
                data = {}
                data["name_sputnik"] = request_data['name_sputnik']
                data["maxcc"] = request_data['maxcc']
                data["time_interval"] = request_data['time_interval']
                data["lat"] = request_data['lat']
                data["long"] = request_data['long']
                data["iLeng"] = request_data['iLeng']
                B02, B03, B04 = download_data(data)
            else:
                return jsonify({"error" : "Wrong sputnik name"})

        if name_sputnik == 'sentinel-1':
            thresh, img, imgTrueColor = analysis_data_sentinel_1(BVV, BVH, sensitivity)
        elif name_sputnik == 'sentinel-2':
            thresh, thresh2, img, imgTrueColor = analysis_data_sentinel_2(B02, B03, B04, type_relief, sensitivity)
        else:
            return jsonify({"error" : "Wrong sputnik name"})

        # Ищем контуры:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # Сортируем найденные контуры по убыванию их длин:
        contours = sorted(contours, key = cv2.contourArea, reverse=True)
        # Составляем список 30 самых длиных контуров:
        cnt = []
        if len(contours) > 0:
            if len(contours) >= 30:
                for i in range(30):
                    cnt.append(contours[i])
            else:
                for i in range(len(contours)):
                    cnt.append(contours[i])
            img2 = img.copy()

            # Накладываем контуры на TrueColor изображение:
            resImg = cv2.drawContours(img, cnt, -1, (0, 0, 255), contour_line_width)

            cnt2 = []
            cntList2 = []

            if name_sputnik == 'sentinel-2' and len(thresh2) > 0:
                # Ищем контуры:
                contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                # Сортируем найденные контуры по убыванию их длин:
                contours2 = sorted(contours2, key = cv2.contourArea, reverse=True)
                # Составляем список 30 самых длиных контуров:
                if len(contours2) >= 30:
                    for i in range(30):
                        cnt2.append(contours2[i])
                else:
                    for i in range(len(contours2)):
                        cnt2.append(contours2[i])
                # Накладываем контуры на TrueColor изображение:
                resImg = cv2.drawContours(resImg, cnt2, -1, (0, 255, 255), contour_line_width)

                # Получаем список контуров в виде списков узловых точек каждого контура:
                cntList2 = json.dumps(cnt2,cls=NumpyEncoder)

            # Получаем список контуров в виде списков узловых точек каждого контура:
            cntList = json.dumps(cnt,cls=NumpyEncoder)

            
            # Превращаем цветную HightLight картинку в список для передачи через json:
            imgTrueColor_rgb = cv2.cvtColor(np.uint8(imgTrueColor), cv2.COLOR_BGR2RGB)
            #imgTrueColor_rgb = cv2.cvtColor(np.uint8(imgTrueColor_rgb), cv2.COLOR_RGB2BGR)
            #encoded_img = json.dumps(np.array(img2).tolist())
            pil_imgTrueColor = Image.fromarray(imgTrueColor_rgb)
            b = io.BytesIO()
            pil_imgTrueColor.save(b, 'jpeg')
            pil_imgTrueColor_bytes = b.getvalue()
            str_imgTrueColor = str(base64.b64encode(pil_imgTrueColor_bytes), encoding='utf-8')#.decode('utf-8')

            # Превращаем цветную картинку в список для передачи через json:
            img2_rgb = cv2.cvtColor(np.uint8(img2), cv2.COLOR_BGR2RGB)
            #img2_rgb = cv2.cvtColor(np.uint8(img2_rgb), cv2.COLOR_RGB2BGR)
            #encoded_img = json.dumps(np.array(img2_rgb).tolist())
            pil_img2 = Image.fromarray(img2_rgb)
            b = io.BytesIO()
            pil_img2.save(b, 'jpeg')
            pil_img2_bytes = b.getvalue()
            str_img2 = str(base64.b64encode(pil_img2_bytes), encoding='utf-8')#.decode('utf-8')

            # Превращаем цветную картинку с нанесенными контурами в список для передачи через json:
            resImg_rgb = cv2.cvtColor(np.uint8(resImg), cv2.COLOR_BGR2RGB)
            #resImg_rgb = cv2.cvtColor(np.uint8(resImg_rgb), cv2.COLOR_RGB2BGR)
            #encoded_resImg = json.dumps(np.array(resImg_rgb).tolist())
            pil_resImg_rgb = Image.fromarray(resImg_rgb)
            b = io.BytesIO()
            pil_resImg_rgb.save(b, 'jpeg')
            pil_resImg_rgb_bytes = b.getvalue()
            str_resImg_rgb = str(base64.b64encode(pil_resImg_rgb_bytes), encoding='utf-8')#.decode('utf-8')
            
            return json.dumps({"contours" : cntList, "contours2" : cntList2, "image" : str_img2, "result_image" : str_resImg_rgb, "hightlight_image" : str_imgTrueColor}, indent=4)
        else:
            return jsonify({"result" : "Count contours = 0"})

if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", port="80")
