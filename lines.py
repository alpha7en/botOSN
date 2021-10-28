import textwrap
import os
from PIL import Image, ImageDraw, ImageFont


def generate_meme(image_path, top_text, bottom_text='', color='#FFFFFF', font_path='ofont.ru_Roboto.ttf', font_size=9,
                  stroke_width=5):
    # load image
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    image_width, image_height = im.size

    # load font
    font = ImageFont.truetype(font=font_path, size=int(image_height * font_size) // 100)

    # convert text to uppercase
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    # text wrapping
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    # draw top lines
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill=color, font=font, stroke_width=stroke_width, stroke_fill='black')
        y += line_height

    # draw bottom lines
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill=color, font=font, stroke_width=stroke_width, stroke_fill='black')
        y += line_height

    # save meme
    os.remove(im.filename.split('/')[-1])
    im.save(im.filename.split('/')[-1])


