import qrcode
import qrcode as qr

# Simple QrCode Generating
''''
img = qr.make("https://www.royalchallengers.com/")

img.save("RCB_APP.png")'''
from PIL import Image
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                   border=5,box_size=20)

qr.add_data('https://www.nationalgeographic.com/')
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color='white')
img.save('National_geographic.png')