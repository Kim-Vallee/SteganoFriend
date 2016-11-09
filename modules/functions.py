from PIL import Image


def RGBToInt(rgb):
    """ Convert a list/tuple with 3 values in rgb one value """
    r, g, b = rgb
    return (r << 16) + (g << 8) + b


def intToRGB(number):
    """ Converts a number into an int tuple """
    r, g, b = number & 255, (number >> 8) & 255, (number >> 16)
    return (r, g, b)


def encodeMessageInFile(image, message):
    """ Creates a new image with the message encoded in it """
    im = Image.open(image)
    pix = im.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            binary = bin(RGBToInt(pix[x, y]))[2:].zfill(24)
            print(binary)
    print(message)
    im.show()