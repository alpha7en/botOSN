from PIL import Image, ImageDraw, ImageFont
import os


def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)

    w, h = original_image.size
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

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))




def r(name):

    o = Image.open(name)
    layer = Image.new('RGB', o.size, 'red') # "hue" selection is done by choosing a color...
    osn = Image.blend(o, layer, 0.5)


    osn = osn.convert("RGBA")
    os.remove(name)
    width, height = osn.size

    scale_image("trim.jpg", 't'+name, width)

    trig = Image.open('t'+name)
    trig = trig.convert("RGBA")
    os.remove('t'+name)

    osn.paste(trig, (0, (height - (trig.size[1]))), mask=trig)

    osn = osn.convert("RGB")
    osn.save(name)
    return

#scale_image('trim.jpg', 't.jpg', 100)
#r("trollface.jpg")
