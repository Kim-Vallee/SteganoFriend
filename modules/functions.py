import base64
import codecs
import binascii

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
    with open(image, "rb") as imageFile:
        byte = imageFile.read()
        binaryFile = bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
        binaryresult = ''
        i = 0
        while i < len(result):
            if i <= 16:
                # On définit le type de ce qu'on encode
                # 00 : message
                # 01 : photo noir et blanc
                # 10 : photo greyscale
                # 11 : photo couleur
                binaryresult += binaryFile[i: i+7] + '0'
            i += 8
        print(result)

def decodeMessage(image):
    """ Decode a message if it exists in a file """
    pass
