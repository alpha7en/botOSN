from PIL import Image, ImageDraw, ImageFont
import os
import random

def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    #original_image = original_image.convert('RGBA')
    w, h = original_image.size
    print(input_image_path)
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
    #original_image = original_image.convert('RGBA')
    original_image.thumbnail(max_size, Image.ANTIALIAS)

    #original_image.save(output_image_path)
    original_image.save(input_image_path[:-3] + 'png')

    scaled_image = Image.open(input_image_path[:-3] + 'png')

    width, height = scaled_image.size
    scaled_image.save(output_image_path)

    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))


def r(name, z = False):
    print(name[:-3] + 'png')
    osna = Image.open(name)
    osna.save(name[:-3] + 'png')
    osna.close()

    osn = Image.open(name[:-3] + 'png')
    os.remove(name)
    osn = osn.convert("RGB")
    os.remove(name[:-3] + 'png')

    width, height = osn.size
    n = 4
    scale_image('{0}.png'.format(n), 't'+name[:-3] + 'png', width=width)

    trig = Image.open('t'+name[:-3] + 'png')

    if z==True:
        osn = osn.transpose(Image.FLIP_LEFT_RIGHT)
    osn.paste(trig, (0, (height - (trig.size[1]))), mask=trig)

    if z==True:
        osn = osn.transpose(Image.FLIP_LEFT_RIGHT)

    osn = osn.convert("RGB")
    osn.save(name[:-3] + 'jpg')
    osn.close()
    trig.close()

    os.remove('t' + name[:-3] + 'png')
    return

#scale_image('trim.jpg', 't.jpg', 100)
if __name__ == "__main__":
    r("m.jpg", z = True)