# Pillow library
from PIL import Image, ImageChops

img1 = Image.open("image1.jpg")
img2 = Image.open("image2.jpg")

image_invert = ImageChops.invert(img1)

image_invert.show()


diff = ImageChops.difference(img1,image_invert)


if diff.getbbox():
    diff.show()
else: print("There is no difference!")