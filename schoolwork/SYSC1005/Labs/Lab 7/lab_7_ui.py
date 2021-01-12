# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from lab_7_filters import *

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
        command = input("L)oad image\nN)egative G)rayscale S)olarize 2)-tone 3)-tone\nQ)uit\n")
        if command == "Q":
            done = True
        elif command == "L":
            img = get_image()
            show(img)
            flag = True
        elif command == "N":
            if not flag:
                print("No image loaded")
            else:
                img = negative(img)
                show(img)
        elif command == "G":
            if not flag:
                print("No image loaded")
            else:
                img = grayscale(img)
                show(img)
        elif command == "2":
            if not flag:
                print("No image loaded")
            else:
                img = black_and_white(img)
                show(img)
        elif command == "3":
            if not flag:
                print("No image loaded")
            else:
                img = black_and_white_and_gray(img)
                show(img)
        elif command == "S":
            if not flag:
                print("No image loaded")
            else:
                thresh = input("Input a threshold value from 0 to 255 inclusive please\n")
                img = solarize(img, int(thresh))
                show(img)
        else:
            print("No such command '" + command + "'")
        