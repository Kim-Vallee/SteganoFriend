#!/usr/bin/env python3

from PIL import Image
import sys
import getopt
import modules


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi::", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> <message>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> <message>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            im = Image.open(arg)
            pix = im.load()
            for x in range(im.size[0]):
                for y in range(im.size[1]):
                    binary = bin(modules.RGBToInt(pix[x, y]))[2:].zfill(24)
                    print(binary)
            im.show()

if __name__ == "__main__":
    main(sys.argv[1:])