import cv2, matplotlib.pyplot as plt

# images are read in the RGB (red, green, blue) format!

def show_image(img):
    plt.imshow(img)
    plt.show()

open_image = cv2.imread("G://WBS - Data Science mit Python//WBS_GroupProject//example_paintings//Alfred_Sisley_63.jpg") 

show_image(open_image)

# showing the maximum koordinaten of an image
# print(open_image.shape)

# showing all pixel values of an image
all_pixel = open_image[0:,0:]
print(all_pixel)


# however comparing all pixel values of an image would't be as effective if the images are slightly manupilated
# that means I might have to compare certain pixel values at certain locations of an image
