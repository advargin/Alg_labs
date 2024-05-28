from PIL import Image
from PIL import ImageOps
import os
from os import listdir

pic = Image.open(os.getcwd() + '/happy something/hb.jpg')
cropped = pic.crop((150, 160, 340, 360))
cropped.save(os.getcwd() + '/cropped.JPEG')
