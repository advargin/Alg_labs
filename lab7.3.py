from PIL import Image
from PIL import ImageOps
import os
from os import listdir

for image in (listdir(os.getcwd() + '/12345')):
    pic = Image.open(os.getcwd() + '/12345/' + image)
    pic = pic.convert('L')
    pic = ImageOps.invert(pic)
    pic = pic.convert('1')
    pic.save(os.getcwd() + '/edited/' + image, 'JPEG')
