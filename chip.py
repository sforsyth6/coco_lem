import cv2
import os
import numpy as np

data = '/raid/data/jhowe/coco/coco-2017/'
dest = '/raid/data/sforsyth/coco_chips/'
size = 224
stride = size*2

for t in ['train', 'val']:

    direc = os.listdir(data + t + '2017/')

    for image in direc:
        img = cv2.imread(data + t + '2017/' + image)

        if img.shape[0]< size or img.shape[1]< size:
                    image_data = cv2.resize(img, (size, size))

        xstride = np.floor((img.shape[0] - size) // stride + 1)
        ystride = np.floor((img.shape[1] - size) // stride + 1)
                        
        xstart = 0
        for x in range(int(xstride)):
            xend = xstart + size
            ystart = 0
            for y in range(int(ystride)):
                yend = ystart + size
                image_chip = img[xstart:xend, ystart:yend, :]
                ystart += stride
                loc = dest + t + '/' + t + '2017/' + str(x) + '-' + str(y) + '-' + image
                cv2.imwrite(loc + '-' + image, image_chip)
            xstart += stride
