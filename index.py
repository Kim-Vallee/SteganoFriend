#!/usr/bin/env python3

from PIL import Image
import sys,getopt


def RGBToInt(rgb):
    """ Convert a list/tuple with 3 values in rgb one value """
    r, g, b = rgb
    return (r << 16) + (g << 8) + b


def intToRGB(number):
    """ Converts a number into an int tuple """
    r, g, b = number & 255, (number >> 8) & 255, (number >> 16)
    return (r, g, b)


args = len(sys.argv)

i = 1
while i < args:
    arg = args[i]
    value = args[i + 1]
    im = Image.open(value)
    pix = im.load()
    size = im.size
    img = Image.new('RGB', size, "black")
    pixels = img.load()
    print((im.size))
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            binary = bin(RGBToInt((pix[x, y]))[2:].zfill(8))
            print(binary)
    i += 1
    img.show()


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print(('Input file is "', inputfile))
    print(('Output file is "', outputfile))