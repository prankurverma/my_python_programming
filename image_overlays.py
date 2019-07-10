import cv2
import numpy as np

# black image
blank_image = np.zeros(shape=[768, 1024, 3], dtype=np.uint8)
# given image
h1 = cv2.imread("/home/prankurverma/Desktop/download.png")

ax,ay = (1024 - h1.shape[1])//2,(768 - h1.shape[0])//2
blank_image[ay:h1.shape[0]+ay,ax:ax+h1.shape[1]] = h1


cv2.imshow('description', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
