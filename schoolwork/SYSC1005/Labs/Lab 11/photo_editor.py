# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from lab_7_filters import *
from filters import *
from scatter import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

if __name__ == "__main__":
    done = False
    flag = False
    while not done:
        command = input("L)oad image\nB)lur E)dge detect P)osterize S)catter T)int sepia\nW)eighted grayscale X)treme contrast\nQ)uit\n")
        if command == "Q":
            done = True
        elif command == "L":
            img = get_image()
            show(img)
            flag = True
        elif command == "B":
            if not flag:
                print("No image loaded")
            else:
                img = blur(img)
                show(img)
        elif command == "E":
            if not flag:
                print("No image loaded")
            else:
                thresh = input("Input a threshold value\n")
                img = detect_edges(img, int(thresh))
                show(img)
        elif command == "P":
            if not flag:
                print("No image loaded")
            else:
                img = posterize(img)
                show(img)
        elif command == "S":
            if not flag:
                print("No image loaded")
            else:
                img = scatter(img)
                show(img)
        elif command == "T":
            if not flag:
                print("No image loaded")
            else:
                img = sepia_tint(img)
                show(img)
        elif command == "W":
            if not flag:
                print("No image loaded")
            else:
                img = weighted_grayscale(image)
                show(img)
        elif command == "X":
            if not flag:
                print("No image loaded")
            else:
                img = extreme_contrast(image)
                show(img)
        else:
            print("No such command '" + command + "'")
        