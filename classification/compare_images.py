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

# Idee: Möglich ist es, wenn ein neues Bild importiert wird, erst mit den Bildern in unserer Datenabnk, 
# welche jeweils einem Künstler zugeornet sind, verglichen wird. 
# wenn das Bild vorhanden ist, dann can das Programm eine genaue Aussage treffen, ansonsten versucht das model eine Prognose abzugeben 