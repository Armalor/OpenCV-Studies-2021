import cv2
import os

img = cv2.imread('../data/road-signs/approaching-a-pedestrian-crossing.jpg')

if img is None:
    print('ФАЙЛ НЕ НАЙДЕН')
    os._exit(1)


img[-10:,-10:] = [255, 0, 0]

print(img.shape)
print(img.size)
# uint8:
print(img.dtype)

img.itemset((10, 10, 0), 255)
print(img.item(10, 10, 0))

# img[:, :, 2] = 0

my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi

cv2.imshow('img', img)


while True:
    key = cv2.waitKey(1)
    if key == 27:
        break;

cv2.destroyAllWindows()
