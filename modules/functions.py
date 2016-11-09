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
    pix = im.load()  # On charge les pixels 1 par 1
    # On crée une image de même taille mais vide
    img = Image.new('RGB', im.size, "black")
    pixels = img.load()
    msg = ''.join([str(bin(ord(x))[2:].zfill(8)) for x in message])
    i = 0
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            original = bin(RGBToInt(pix[x, y]))[2:].zfill(24)
            print(original)
            modified = original[:-2] + msg[i:i + 2].zfill(2)
            print(modified)
            print('\n\n')
            pixels[x, y] = intToRGB(int(modified, 2))
            i += 2
    img.show()