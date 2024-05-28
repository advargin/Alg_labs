from PIL import Image
from PIL import ImageOps
import os
from os import listdir

postcard_index = {'день огурца': 'cucumper.jpg', 'день рождения': 'hb.jpg', 'день цемента': 'concrete.png',
                  'день ковра': 'carpet.jpg', }
reason = input('К какому празднику ему нужна открытка?').strip()
postcard = Image.open(os.getcwd() + '/happy something/' + postcard_index[reason])
postcard.show()
