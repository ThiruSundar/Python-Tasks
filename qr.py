# generate qr code

# import pyqrcode
# qr = pyqrcode.create('Welcome Mr. Stark')
# qr.png('testqr.png', scale=10)

#  read qr code

from pyzbar.pyzbar import decode
from PIL import Image
dec = decode(Image.open('testqr.png'))
print(dec[0].data.decode('ascii'))