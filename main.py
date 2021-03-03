import cv2
import numpy as np
import os

def hemorrhages(image):

    img = cv2.resize(image, (800, 615))

    p = img.shape
    print(p)


    #extract green channel and improve contrast
    blue, green, red = cv2.split(img)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_green = clahe.apply(green)
    #print(enhanced_green)

    #add thresholding
    ret, th1 = cv2.threshold(enhanced_green, 30, 255, cv2.THRESH_BINARY)

    #apply dialtion
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(th1, kernel, iterations=1)

    return dilation


image = cv2.imread('E:/final_project/github_projects/bale_project/sampleImages/hemorrhages/1.jpg')
output = hemorrhages(image)
cv2.imwrite('output.png', output)
cv2.imshow('output', output)
cv2.waitKey(0)