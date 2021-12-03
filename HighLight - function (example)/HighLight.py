import cv2
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

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

imgB02 = Image.open('B02.jpg',mode='r')
B02 = np.asarray(imgB02)
imgB03 = Image.open('B03.jpg',mode='r')
B03 = np.asarray(imgB03)
imgB04 = Image.open('B04.jpg',mode='r')
B04 = np.asarray(imgB04)

img1 = np.zeros((B02.shape[0], B02.shape[1], 3))
img1[:,:,0] = B04/100
img1[:,:,1] = B03/100
img1[:,:,2] = B02/100

# Создаем пустое изображение:
# Создаем цветовую палитру по имени:
cm2 = plt.get_cmap('gist_rainbow')
# Применяем цветовую палитру к массиву:
colored_image = cm2(B02)
# Полученную картинку с 4-мя каналами (R,G,B,A) с значениями float[0, 1] конвертируем в RGB(uint8):
imgcc = Image.fromarray((colored_image[:, :, :3] * 255).astype(np.uint8))
imgTrueColor = np.asarray(imgcc)

# Создаем массивы данных для создания HighLight-изображения:
height, width, _ = img1.shape
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

# Превращаем цветную HightLight картинку в список для передачи через json:
imgTrueColor_rgb = cv2.cvtColor(np.uint8(imgTrueColor), cv2.COLOR_BGR2RGB)
pil_imgTrueColor = Image.fromarray(imgTrueColor_rgb)
b = io.BytesIO()
pil_imgTrueColor.save(b, 'jpeg')
pil_imgTrueColor_bytes = b.getvalue()
str_imgTrueColor = str(base64.b64encode(pil_imgTrueColor_bytes), encoding='utf-8')

# Извлекаем из Json:
hightlight_image = Image.open(io.BytesIO(base64.b64decode(str_imgTrueColor)))
img3 = np.asarray(hightlight_image)

# Строим картинки:
plt.subplot(2,2,1)
plt.imshow(img1)
plt.title('Image')
plt.axis("on")
plt.subplot(2,2,2)
plt.imshow(hightlight_image)
plt.title('HighLight Image')
plt.axis("on")

# Строим гистограммы:
plt.subplot(2,2,3)
plt.hist(img1[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
plt.hist(img1[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
plt.hist(img1[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
plt.xlabel('Intensity Value')
plt.ylabel('Count')
plt.legend(['Red_Channel', 'Green_Channel', 'Blue_Channel'])
plt.xlim([0, 1])
plt.ylim([0, 70000])
plt.title('Image')

plt.subplot(2,2,4)
plt.hist(img3[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
plt.hist(img3[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
plt.hist(img3[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
plt.xlabel('Intensity Value')
plt.ylabel('Count')
plt.legend(['Red_Channel', 'Green_Channel', 'Blue_Channel'])
plt.xlim([-0.5, 255.5])
plt.ylim([0, 15000])
plt.title('HighLight image')
plt.show()
