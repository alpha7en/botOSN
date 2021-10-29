from PIL import Image, ImageDraw, ImageFont
import os


def r(name, text):
    osn = Image.open(name)
    osn = osn.convert("RGBA")
    os.remove(name)
    width, height = osn.size
    # print(width, height)

    testText = ImageFont.truetype('ofont.ru_Roboto.ttf', size=1)
    wid, hei = testText.getsize(text)
    print(wid, hei)
    print(width * 2.3, height * 0.5)
    print(int((height * 0.5) / hei), int((width * 2) / wid))
    if int((height * 0.5) / hei) < int((width * 2) / wid):
        size = int((height * 0.5) / hei)
    else:
        size = int((width * 2) / wid)

    font = ImageFont.truetype('ofont.ru_Roboto.ttf', size=size)

    img = Image.new("RGBA", (int(width * 1.4), int(height * 1.5)))

    b = Image.new("RGBA", (int(width * 1.03), int(height * 1.03)), color=(0, 0, 0))
    x = int((b.size[0] / 2) - (osn.size[0] / 2))
    y = int((b.size[1] / 2) - (osn.size[1] / 2))
    b.paste(osn, (x, y), mask=osn)
    w = Image.new("RGBA", (int(width * 1.06), int(height * 1.06)), color=(255, 255, 255))
    x = int((w.size[0] / 2) - (b.size[0] / 2))
    y = int((w.size[1] / 2) - (b.size[1] / 2))
    w.paste(b, (x, y), mask=b)
    img = img.convert("RGB")
    img.save(name)
    im2 = Image.open(name)

    x = int((im2.size[0] / 2) - (w.size[0] / 2))
    y = int((im2.size[1] / 2) - (w.size[1] / 2) - height * 0.3)

    # im2.paste(w, (x, y), mask=w)
    # im2 = im2.convert("RGB")
    im2.paste(w, (x, w.size[1] // 12), mask=w)
    draw = ImageDraw.Draw(im2)
    l, h = draw.textsize(text, font=font)
    wi = im2.size[0]
    vrem = (im2.size[1] - ((13 * w.size[1]) / 12)) // 2 - h // 2
    draw.text((int(wi / 2 - l * 0.5), int(((13 * w.size[1]) / 12) + vrem)), text + ' ', font=font, fill=('#FFFFFF'))
    os.remove(name)
    im2.save(name)

    return

#r("mem1.jpg","lol")
