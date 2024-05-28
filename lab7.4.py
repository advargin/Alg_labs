from PIL import Image
from PIL import ImageOps
import os
from os import listdir

for image in (listdir(os.getcwd() + '/12345')):
    pic = Image.open(os.getcwd() + '/12345/' + image)
    mark = Image.open(os.getcwd() + '/copyright-free-image.jpg')

    pic.paste(mark, (50, 50))
    pic.save(os.getcwd() + '/watermark/' + image, 'JPEG')
