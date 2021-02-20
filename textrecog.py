# read text from image

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract'
from PIL import Image
pic = Image.open('new.png')
string = tess.image_to_string(pic)
print(string)