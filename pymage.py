"""Image manipulation in python

Image manipulation like resizing for a large number of
images at the same time.

Author: William Noris w.noris@protonmail.com
Created: 20/07/2022
"""
import math
from PIL import Image


def main():
    print("Bienvenue dans le programme de manipulation d'images.")
    img = Image.open("img.jpg")
    (w, h) = img.size
    newSize = (math.floor(w/2), math.floor(h/2))
    imgResized = img.resize(newSize)
    imgResized.save("img-copie.jpg")


if __name__ == "__main__":
    print("coucou")
    main()
