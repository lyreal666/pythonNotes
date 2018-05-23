#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

with Image.open('./imgs/miaye.jpg') as im:
    print(type(im))
    w, h = im.size
    print('width: %s,height: %s' % (w, h))
    im.thumbnail((w//2, h//2))
    print('the pic is thumbnailed %d,%d' % (w//2, h//2))
    im.save('./imgs/thumbnail_miaye.jpg')
    im.filter(ImageFilter.BLUR)
    im.save('./imgs/thumbnail_blur_miaye.jpg', 'jpeg')

with Image.open('./imgs/miaye.jpg') as im:
    print(type(im))
    w, h = im.size
    im.filter(ImageFilter.BLUR)
    im.save('./imgs/blur_miaye.jpg', 'jpeg')


def rndChar():
    return chr(random.randint(65, 90))


def rand_color1():
    return random.randint(123, 255), random.randint(123, 255), random.randint(123, 255)


def rand_color2():
    return random.randint(25, 123), random.randint(25, 123), random.randint(25, 123)


width = 60 * 4
height = 60
im = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('./fonts/CanelaBark_PERSONAL.ttf', 36)
imd = ImageDraw.Draw(im)
for x in range(width):
    for y in range(height):
        imd.point((x, y), fill=rand_color2())

for w in range(4):
    imd.text((60 * w + 10, 10), rndChar(), font=font, fill=rand_color1())
im.filter(ImageFilter.BLUR)
im.save('./imgs/code.jpg', 'jpeg')