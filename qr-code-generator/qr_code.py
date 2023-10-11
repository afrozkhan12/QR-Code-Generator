import  qrcode  as  qr 
from PIL import Image

qr = qr.QRCode(version= 1,
                   error_correction = qr.constants.ERROR_CORRECT_H,
                   box_size= 8, border = 4,)
qr.add_data("https://github.com/afrozkhan12?tab=repositories")
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
img.save("code.jpeg")
qr._mask_pattern: copyright
