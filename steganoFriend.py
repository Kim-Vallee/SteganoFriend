#!/usr/bin/env python3

import sys
import argparse
import modules
import os.path

parser = argparse.ArgumentParser(description="This program hides a message\
                                              into an RGB image")

def main(argv):
    bgroup = parser.add_argument_group("Hide message with LSB method")
    bgroup.add_argument('-image', help='Provide the original image')
    bgroup.add_argument('-message', help='The message to hide in the image')
    bgroup.add_argument('-output', help='Provide the name of the output')
    bgroup.add_argument('-format', help='Provide the output format of the file, default is jpeg')
    bgroup = parser.add_argument_group("Reveal message in a picture")
    bgroup.add_argument('-stegfile', help='Provide the steganographic image')
    bgroup.add_argument('-out', help='Provide output file: default just print')

    args = parser.parse_args(argv[1:])

    arguments = len(argv)

    if arguments == 7:
        modules.encodeMessageInFile(args.image, args.message, args.output, "jpg")
    elif arguments == 3:
        print(modules.decodeMessage(args.stegfile))
    else:
        print("Usage: '", argv[0], "-h' for help", "\n", args)

if __name__ == "__main__":
    main(sys.argv)
