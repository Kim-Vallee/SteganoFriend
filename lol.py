#!/usr/bin/env python3

from PIL import Image
import sys, math, random


def RGBToInt(rgb):
    """ Convert a list/tuple with 3 values in rgb one value """
    r, g, b = rgb
    return (r << 16) + (g << 8) + b


def intToRGB(number):
    """ Converts a number into an int tuple """
    r, g, b = number & 255, (number >> 8) & 255, (number >> 16)
    return (r, g, b)

for infile in sys.argv[1:]:
    im = Image.open(infile)  # Opening file
    pix = im.load()  # Init pixels
    img = Image.new('RGB', (255, 255), "black")  # create a new black image
    pixels = img.load()  # create the pixel map
    for x in range(img.size[0]):  # For pixels in x row
        for y in range(img.size[1]):  # For pixels in y column
            intRGB = RGBToInt(pix[x, y])
            binaryRGB = bin(intRGB)[2:].zfill(24)
            pixels[x, y] = (1, 1, (x ** 2 % (y + 1)) ** 2 % 255)
    img.show()
