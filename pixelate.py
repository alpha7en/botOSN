from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import os

def r(name, pixel_size=9, draw_margin=True):
    image = Image.open(name)
    margin_color = (0, 0, 0)
    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    pixel = image.load()
    # Draw black margin between pixels
    if draw_margin:
        for i in range(0, image.size[0], pixel_size):
            for j in range(0, image.size[1], pixel_size):
                for r in range(pixel_size):
                    pixel[i+r, j] = margin_color
                    pixel[i, j+r] = margin_color
    os.remove(name)
    image.save(name)
    return