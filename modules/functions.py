
def RGBToInt(rgb):
    """ Convert a list/tuple with 3 values in rgb one value """
    r, g, b = rgb
    return (r << 16) + (g << 8) + b


def intToRGB(number):
    """ Converts a number into an int tuple """
    r, g, b = number & 255, (number >> 8) & 255, (number >> 16)
    return (r, g, b)


def encodeMessageInFile(image, message, ofile, f):
    """ Creates a new image with the message encoded in it """
    pass

def decodeMessage(image):
    """ Decode a message if it exists in a file """
    pass
