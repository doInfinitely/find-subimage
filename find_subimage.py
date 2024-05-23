import cv2
import random
import numpy as np

image = cv2.imread("YJvynCW.jpeg")
height, width, channels = image.shape
image = cv2.resize(image, (width//16,height//16))
height, width, channels = image.shape
subimage_size = (32,32)
x,y = random.randrange(width-subimage_size[0]), random.randrange(height-subimage_size[1])
subimage = image[y:y+subimage_size[1], x:x+subimage_size[0]]

mini = (float("inf"), -1, -1)
for i in range(width-subimage_size[0]):
    for j in range(height-subimage_size[1]):
        diff = np.linalg.norm(image[j:j+subimage_size[1], i:i+subimage_size[0]]-subimage)
        if diff < mini[0]:
            mini = (diff, i, j)

print(x,y)
print(mini)
