import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# data = "https://pypi.org/project/qrcode/"
# filename = "qrcode.png"
# # box_size = 18,
# # border = 5,
# img = qrcode.make(data)
# type(img)
# img.save(filename)

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('https://docs-python.ru/packages/generator-qr-kodov/')
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, module_drawe=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage,
                      embeded_image_path="C:/Users/alexh/PycharmProjects/Various/images/14.jpeg")
img_1.save("111.png")
img_2.save("222.png")
img_3.save("333.png")

#############

import shutil
total_b, usage_b, free_b = shutil.disk_usage(' . ')

gb = 10 ** 9

print('Total: {:6.2f} GB'. format(total_b / gb))
print('Used: {:6.2f} GB'. format(usage_b / gb))
print('Free: {:6.2f} GB'. format(free_b / gb))