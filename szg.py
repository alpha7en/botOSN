from PIL import Image
import os
def r(name, mode):
    image = Image.open(name)
    #print(name)

    x, y = image.size
    print(x,y)
    if mode == 1:
        ou = image.resize((x//4, y))
    else:
        ou = image.resize((x, y//4))
    os.remove(name)
    ou.save(name)
    # сжатие
    return