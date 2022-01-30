import qrcode

data = "https://pypi.org/project/qrcode/"
filename = "qrcode.png"
# box_size = 18,
# border = 5,
img = qrcode.make(data)
type(img)
img.save(filename)