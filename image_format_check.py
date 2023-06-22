import matplotlib.pyplot as plt
from PIL import Image
# import 


im = plt.imread("example_paintings\Edgar_Degas_101.jpg")
print(im.dtype)
im_pil = Image.open("example_paintings\Edgar_Degas_101.jpg")
print(im_pil.format)
print(im_pil.size)
print(im_pil.mode)