"""Image manipulation in python

Image manipulation like resizing for a large number of
images at the same time.

Author: William Noris w.noris@protonmail.com
Created: 20/07/2022
"""

import math
import argparse
from PIL import Image
import os
import time


def parseFiles(rawFilesArg):
    """ Récupère la liste des fichiers a transformer donnés en ligne de commande et les renvoie dans une liste"""

    filesList = []
    if os.path.isfile(rawFilesArg) == True:
        filesList.append(rawFilesArg)
    else:
        if os.path.exists(rawFilesArg) == True:
            # L'argument entré est un dossier. On extrait donc tous les fichiers de celui-ci
            for f in os.walk(rawFilesArg):
                filesList.append(f)
        else:
            filesToCheck = rawFilesArg.split(',')
            for f in filesToCheck:
                if (os.path.exists(f)):
                    filesList.append(f)
    return filesList


def noSubExit(args):
    print("No sub command provided. Exiting...")
    exit(1)


def generateDirName(prefix):
    t = time.localtime()
    return prefix + str(t.tm_year) + str(t.tm_mon) + str(t.tm_yday) + str(t.tm_hour) + str(t.tm_min) + str(t.tm_sec)


def performResize(files):

    dirName = generateDirName("resize_")
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:
        print("Le dossier de destination existe deja...")
        exit(1)

    for f in files:
        print(f"Resizing {f}")
        img = Image.open(f)
        (w, h) = img.size
        newSize = (math.floor(w/2), math.floor(h/2))
        imgResized = img.resize(newSize)

        imgResized.save(dirName + "/" + f)


def resize(args):
    print("Resizing images...")
    print("------------------")
    performResize(parseFiles(args.files))


def main():
    # Top level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title='subcommands', description='valid subcommands', help='additional help')
    parser.set_defaults(func=noSubExit)

    # parsers for subcommands
    parserResize = subparsers.add_parser(
        'resize', help="Divise par deux la taille des images.")
    parserResize.add_argument(
        '-f', '--files', help="Dossier, fichier, ou liste de fichiers séparés par des virgules")
    parserResize.set_defaults(func=resize)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
