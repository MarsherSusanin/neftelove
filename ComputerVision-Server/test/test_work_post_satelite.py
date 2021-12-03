import json
import requests
import cv2
import numpy as np
import PIL.Image as Image
#from skimage import io
import io
import matplotlib.pyplot as plt
import base64

from scipy.signal import argrelextrema, resample
from scipy import interpolate

"""
def get_image(f):
    im = Image.open(f,mode='r')#.convert('L')
    im2 = np.asarray(im, dtype='uint8')
    encoded_im = json.dumps(np.array(im2).tolist())
    return encoded_im
"""

def get_image(f):
    pil_resImg_rgb = Image.open(f,mode='r')
    b = io.BytesIO()
    pil_resImg_rgb.save(b, 'jpeg')
    pil_resImg_rgb_bytes = b.getvalue()
    str_resImg_rgb = str(base64.b64encode(pil_resImg_rgb_bytes), encoding='utf-8')#.decode('utf-8')
    return str_resImg_rgb

#url = "http://192.168.0.16/getcontours"
url = "http://172.20.10.11:80/getcontours"
#url = "http://34.125.19.61/getcontours"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

"""
data = {
        "download_data" : "download",
        "name_sputnik" : "sentinel-1",
        "maxcc" : "20",
        "time_interval" : "2021-08-08/2021-08-10",
        "lat" : "44.469596",
        "long" : "37.133366",
        "iLeng" : "100"
    }
"""


data = {
        "download_data" : "download",
        "name_sputnik" : "sentinel-2",
        "type_relief" : "1", # 0 - суша, 1 - речка, 2 - море
        "maxcc" : "55",
        #"time_interval" : "2020-06-01T00:00:00.000Z/2020-06-02T00:00:00.000Z",
        "time_interval" : "2020-05-31/2020-06-01",
        "lat" : "69.44226749127356",
        "long" : "87.88040824890137",
        "iLeng" : "10"
    }


"""
data = {
        "download_data" : "exist",
        "name_sputnik" : "sentinel-1",
        "image_VV" : get_image("VV.jpg"),
        "image_VH" : get_image("VH.jpg")
    }
"""

"""
data = {
        "download_data" : "exist",
        "name_sputnik" : "sentinel-2",
        "type_relief" : "1", # 0 - суша, 1 - речка, 2 - море
        "image_B02" : get_image("B02.jpg"),
        "image_B03" : get_image("B03.jpg"),
        "image_B04" : get_image("B04.jpg")
    }
"""

"""
data = {
        "download_data" : "exist",
        "name_sputnik" : "sentinel-2",
        "type_relief" : "1", # 0 - суша, 1 - речка, 2 - море
        "image_B02" : get_image("B02_2.jpg"),
        "image_B03" : get_image("B03_2.jpg"),
        "image_B04" : get_image("B04_2.jpg")
    }
"""

r = requests.post(url, data=json.dumps(data), headers=headers)

if r.status_code == 200:
    print(r)
    rs = r.json()
    print(rs)

    #print(rs["image"])

    #print(rs["contours"])
    
    #img = Image.fromarray(np.array(json.loads(rs["image"]), dtype='uint8'))
    img = Image.open(io.BytesIO(base64.b64decode(rs["image"])))
    img1 = np.asarray(img)
    img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    #cv2.imshow('img1',img_rgb)
    plt.imshow(img_rgb)
    plt.axis("on")
    plt.show()

    #resImg = Image.fromarray(np.array(json.loads(rs["result_image"]), dtype='uint8'))
    resImg = Image.open(io.BytesIO(base64.b64decode(rs["result_image"])))
    img2 = np.asarray(resImg)
    resImg_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    #cv2.imshow('img2',resImg_rgb)
    plt.imshow(resImg_rgb)
    plt.axis("on")
    plt.show()

    
    hightlight_image = Image.open(io.BytesIO(base64.b64decode(rs["hightlight_image"])))
    img3 = np.asarray(hightlight_image)
    hightlight_image_rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
    #cv2.imshow('img3',hightlight_image_rgb)
    plt.imshow(hightlight_image_rgb)
    plt.axis("on")
    plt.show()

    #plt.hist(img1.ravel(), bins = 256, color = 'orange', )
    plt.hist(img1[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
    plt.hist(img1[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    plt.hist(img1[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
    plt.xlabel('Intensity Value')
    plt.ylabel('Count')
    plt.legend(['Red_Channel', 'Green_Channel', 'Blue_Channel'])
    plt.xlim([-0.5, 255.5])
    plt.ylim([0, 300])
    plt.title('Image')
    plt.show()

    

    # Строим гистограмму красного канала:
    hi0, countshi0 = np.histogram(img3[:, :, 0], range(256))#img3[:, :, 0].ravel()
    hi1, countshi1 = np.histogram(img3[:, :, 1], range(256))#hi1 = img3[:, :, 1].ravel()
    #hi2 = img3[:, :, 2].ravel()

    plt.figure()
    plt.subplot()
    plt.plot(hi0)
    plt.xlim([-0.5, 255.5])
    plt.ylim([0, 150])
    plt.title('HighLight Red channel')
    #plt.axis("off")
    plt.show()

    plt.figure()
    plt.subplot()
    plt.plot(hi1)
    plt.xlim([-0.5, 255.5])
    plt.ylim([0, 150])
    plt.title('HighLight Green channel')
    #plt.axis("off")
    plt.show()

    # Сглаживание
    x = np.linspace(0, 255, len(hi0))
    #print(len(hi0))
    #xnew = np.linspace(x.min(), x.max(), len(hi0)*10) 
    #bspline = interpolate.make_interp_spline(x, hi0)
    #smooth_hi0 = bspline(xnew)

    window_len = 10
    while True:
        window_len += 1
        kernel = np.ones(window_len, dtype=float)/window_len
        smooth_hi0 = np.convolve(hi0, kernel, 'same')
        minHi0 = np.array(argrelextrema(smooth_hi0, np.less)[0])
        if minHi0.size <=2:
            break
    if len(minHi0) < 2:
        minHi0 = np. concatenate( (minHi0, [245] ) )
    if minHi0[1] < 200:
        minHi0[1] = 245

    print(minHi0)

    window_len = 10
    while True:
        window_len += 1
        kernel = np.ones(window_len, dtype=float)/window_len
        smooth_hi1 = np.convolve(hi1, kernel, 'same')
        minHi1 = np.array(argrelextrema(smooth_hi1, np.less)[0])
        if minHi1.size <= 5:
            break

    print(minHi1)
    
    plt.plot(x, smooth_hi0)
    plt.xlim([-0.5, 255.5])
    plt.ylim([0, 150])
    plt.title('Smoothed HighLight Red channel')
    plt.show()

    plt.plot(x, smooth_hi1)
    plt.xlim([-0.5, 255.5])
    plt.ylim([0, 150])
    plt.title('Smoothed HighLight Green channel')
    plt.show()
    
    #hi0[argrelextrema(hi0, np.less)[0]] #np.greater
    
    #print(argrelextrema(smooth_hi1, np.less))

    #plt.hist(img3.ravel(), bins = 256, color = 'orange', )
    plt.hist(img3[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
    plt.hist(img3[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    plt.hist(img3[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
    plt.xlabel('Intensity Value')
    plt.ylabel('Count')
    plt.legend(['Red_Channel', 'Green_Channel', 'Blue_Channel'])
    plt.xlim([-0.5, 255.5])
    plt.ylim([0, 300])
    plt.title('HighLight image')
    plt.show()
