from PIL import Image, ImageChops
import os
def r(name):
    i1 = Image.open(name)
    i2 = Image.open(name[:-4]+'v.jpg')

    n = ImageChops.multiply(i1, i2)
    os.remove(name)
    os.remove(name[:-4] + 'v.jpg')
    n.save(name)