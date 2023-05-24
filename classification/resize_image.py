import cv2
import matplotlib.pyplot as plt

img = cv2.imread("G://WBS - Data Science mit Python//WBS_GroupProject//example_paintings//Alfred_Sisley_63.jpg")

img2 = cv2.resize(img, (32,32),300,300,cv2.INTER_LINEAR)


print("Image Width is", img2.shape[1])
print("Image Height is", img2.shape[0])