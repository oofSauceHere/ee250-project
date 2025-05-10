import cv2
import numpy as np

# read image
img = cv2.imread("Handwriting-Transformers/results/image0.png")
height, width, _ = img.shape

# crop image
cropped = img[0:height//8, 725:width]

# write image
cv2.imwrite("out/cropped.png", cropped)

# wow!