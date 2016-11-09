#!/usr/bin/env python3

import sys
import getopt
import modules


def main(argv):
    message = ''  # Plus facile à vérifier si jamais l'option est inutilisé
    infile = ''
    helpMessage = "test.py -i <inputfile> -m <message>"  # Message d'erreur
    try:
        # On récupère les arguments et leur valeurs
        opts, args = getopt.getopt(argv, "hi:m:", ["ifile=", "message="])
    except getopt.GetoptError:
        # Mauvaise utilisation des arguments
        print(helpMessage)
        sys.exit(2)
    for opt, arg in opts:  # On parcours les arguments
        if opt == '-h':  # Message d'aide demandé
            print(helpMessage)
            sys.exit()
        elif opt in ("-i", "--ifile"):  # On récupère le nom du fichier
            infile = arg
        elif opt in ("-m", "--message"):  # On récupère le message à encoder
            message = arg
    try:  # Si jamais l'utilisateur ne met que le message ou que le fichier...
        if message == '' or infile == '':
            raise getopt.GetoptError  # On lève une erreur
        modules.encodeMessageInFile(infile, message)
    except:
        print(helpMessage)
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])