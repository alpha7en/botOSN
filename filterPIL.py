from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import random
import os

def pixelate(image, pixel_size=9, draw_margin=True):
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

    return image

def filter(name):
	image = Image.open(name)
	mode = random.randint(1, 5)
	if mode == 1:
		new= image.filter(ImageFilter.CONTOUR)
	if mode == 2:
		new= image.convert("1")
	if mode == 3:
		new= image.convert("L")
	if mode == 4:
		s = random.randint(4, 50)
		new= pixelate(image, pixel_size=s)
	if mode == 5:
		mirror = image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
		sz     = max(image.size + mirror.size)
		new = Image.new(image.mode, (sz,sz))
		new.paste(image, (0,0)+image.size)
# now paste the mirrored image, but with a triangular binary mask
		mask = Image.new('1', mirror.size)
		draw = ImageDraw.Draw(mask)
		draw.polygon([0,0,0,sz,sz,sz], outline='white', fill='white')
		new.paste(mirror, (0,0)+mirror.size, mask)

	os.remove(name)
	new.save(name)
	return


