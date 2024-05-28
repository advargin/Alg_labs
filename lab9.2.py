from PIL import Image
from PIL import ImageOps
import os
from os import listdir

for image in (listdir(os.getcwd() + '/12345')):
    if not image.endswith('.jpg'):
        continue
    pic = Image.open(os.getcwd() + '/12345/' + image)
    pic = pic.convert('L')
    pic = ImageOps.invert(pic)
    save_patch = os.getcwd() + '/lab9.1/'
    if not os.path.exists(save_patch):
        os.makedirs(save_patch)
    pic.save(save_patch + 'edited' + image, 'JPEG')
