from PIL import Image

pic = Image.open('hamster.jpg')
small_hamster = pic.reduce(10)
small_hamster.save('small_hamster.jpg')
rotated_hamster = pic.rotate(20)
rotated_hamster.save('rotated_hamster.jpg')
flipped_hamster = pic.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
flipped_hamster = flipped_hamster.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
flipped_hamster.save('flipped_hamster.jpg')
