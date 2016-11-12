from PIL import Image


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
    im = Image.open(image)
    pix = im.load()  # On charge les pixels 1 par 1
    # On crée une image de même taille mais vide
    img = Image.new('RGB', im.size, "black")
    pixels = img.load()
    msg = ''.join([str(bin(ord(x))[2:].zfill(8)) for x in message])
    msg += bin(3)[2:].zfill(8) # On ajoute le charactère de fin
    i = 0
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = pix[x, y]
            r, g, b = bin(r)[2:].zfill(8), bin(g)[2:].zfill(8), bin(b)[2:].zfill(8)
            r1 = g1 = b1 = ""
            r1 += r[:7] + msg[i:i + 1].zfill(1)  # [i: i + 1] avoids index out of range
            g1 += g[:7] + msg[i + 1: i + 2].zfill(1)
            b1 += b[:7] + msg[i + 2: i + 3].zfill(1)
            r, g, b = int(r1, 2), int(g1, 2), int(b1, 2)
            pixels[x, y] = (r, g, b)
            if i == 0:
                print(pixels[x,y])
            i += 3
    img.save(ofile + '.' + f)

def decodeMessage(image):
    """ Decode a message if it exists in a file """
    byte = ''
    message = ''
    im = Image.open(image)
    pix = im.load()  # On charge les pixels 1 par 1
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = pix[x,y]
            if x == 0 and y == 0:
                print(pix[x,y])
            r, g, b = bin(r)[2:].zfill(8), bin(g)[2:].zfill(8), bin(b)[2:].zfill(8)
            byte += r[7] + g[7] + b[7]
            if len(byte) == 8:
                if int(byte, 2) == 3:
                    return message
                else:
                    message += chr(int(byte, 2))
                    byte = ''
    return message
