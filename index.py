#!/usr/bin/env python3

from PIL import Image
import sys


def RGBToInt(rgb):
    """ Convert a list/tuple with 3 values in rgb one value """
    r, g, b = rgb
    return (r << 16) + (g << 8) + b


def intToRGB(number):
    """ Converts a number into an int tuple """
    r, g, b = number & 255, (number >> 8) & 255, (number >> 16)
    return (r, g, b)


for infile in sys.argv[1:]:
    im = Image.open(infile)
    pix = im.load()
    size = im.size
    img = Image.new('RGB', size, "black")
    pixels = img.load()
    print((im.size))
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            binary = bin(RGBToInt((pix[x, y]))[2:].zfill(8))
            print(binary)

img.show()
