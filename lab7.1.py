from PIL import Image

pic = Image.open('hamster.jpg')
# pic.show()
print(pic.size, pic.format)
