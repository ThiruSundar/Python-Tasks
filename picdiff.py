from PIL import Image, ImageChops

img1 = Image.open('pic1.jpg')
img2 = Image.open('pic2.jpg')

diff = ImageChops.difference(img1 , img2)

# print(diff.getbbox())

if diff.getbbox():
    diff.show()