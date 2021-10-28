from PIL import Image,ImageFilter, ImageDraw, ImageFont
import os
import random

def dr(name, n, args = ['50', '#1C0606']):
    print(args)
    size = int(args[0])
    original = Image.open(name)
    original.load()
    font = ImageFont.truetype('ofont.ru_Roboto.ttf', size=size)

    x = original.size
    draw_text = ImageDraw.Draw(original)
    draw_text.text(
        (x[0] - ((len(n)-1)*size + 40), x[1] - (size + 40)),
        n,
        font=font,
        fill=(args[1])
    )
    # mode = random.randint(1, 4)
    # print(mode)
    # if mode == 1:
    #     new = original.filter(ImageFilter.CONTOUR)
    # elif mode == 2:
    #     new = original.filter(ImageFilter.SMOOTH)
    # elif mode == 3:
    #
    # elif mode == 4:
    #     new = original.filter(ImageFilter.EMBOSS)

    os.remove(name)
    original.save(name)
    return
