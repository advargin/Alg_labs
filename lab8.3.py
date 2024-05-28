from PIL import Image, ImageOps, ImageDraw, ImageFont
import os
from os import listdir

postcard_index = {'день огурца': 'cucumper.jpg', 'день рождения': 'hb.jpg', 'день цемента': 'concrete.png',
                  'день ковра': 'carpet.jpg', }
reason = input('К какому празднику ему нужна открытка?').strip()
personal_text = input('А как вас зовут?').strip() + 'ПОЗДРАВЛЯЮ!!!!!'
postcard = Image.open(os.getcwd() + '/happy something/' + postcard_index[reason])
font_type = ImageFont.truetype(font="Arial Bold", size=30)
draw = ImageDraw.Draw(postcard)
draw.text(xy=(50, 150), text=personal_text, font=font_type, stroke_width=10, stroke_fill='red')
postcard.show()
