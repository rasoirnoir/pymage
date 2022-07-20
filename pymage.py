"""Image manipulation in python

Image manipulation like resizing for a large number of
images at the same time.

Author: William Noris w.noris@protonmail.com
Created: 20/07/2022
"""
from ast import parse
import math
import argparse
from PIL import Image

_FILES = "./"


def resize():
    print(f"Resize the image !! {_FILES}")


def parse():
    # Top level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title='subcommands', description='valid subcommands', help='additional help')

    # parsers for subcommands
    parserResize = subparsers.add_parser('resize')
    parserResize.add_argument(
        '-f', '--files', help="Dossier, fichier, ou liste de fichies séparés par des virgules")
    parserResize.set_defaults(func=resize)
    args = parser.parse_args()
    _FILES = args.files
    print(f"_FILES: {_FILES}, argument: {args.files}")
    args.func()


def main():
    print("Bienvenue dans le programme de manipulation d'images.")
    img = Image.open("img.jpg")
    (w, h) = img.size
    newSize = (math.floor(w/2), math.floor(h/2))
    imgResized = img.resize(newSize)
    imgResized.save("img-copie.jpg")


if __name__ == "__main__":
    parse()
    main()
