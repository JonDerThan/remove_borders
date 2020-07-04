import os

import numpy as np
import cv2

# Used for border-detection. Every border with colors under this threshhold should be removed.
max_color = [10, 10, 10]

def main():
    # Directory with input images.
    dir0 = "./data/"

    # Directory name for output images.
    outdir0 = "./out/"

    # Gets every file out of the input directory.
    files0 = [f for f in os.listdir(dir0) if os.path.isfile(os.path.join(dir0, f))]

    # Creates the output directory if it does not already exist.
    if not os.path.isdir(outdir0):
        os.mkdir(outdir0)

    for file0 in files0:
        img0 = os.path.join(dir0, file0)
        out0 = os.path.join(outdir0, file0)

        img = cv2.imread(img0)

        out = remove_borders(img)

        cv2.imwrite(out0, out)

# Wrapper method for every border removal method.
def remove_borders(img):
    img = remove_top_border(img)
    img = remove_bottom_border(img)
    img = remove_left_border(img)
    img = remove_right_border(img)

    return img



# START BORDER REMOVAL METHODS

# Recursive methods for border removal. If one line/row of pixels only contains colors under the specified threshhold ("max_color") it gets removed and the method repeats itself.

def remove_top_border(img):
    if (img[0] <= max_color).all():
        # Cuts one horizontal row on top.
        return remove_top_border(img[1:])

    else:
        return img

def remove_bottom_border(img):
    if (img[-1] <= max_color).all():
        # Cuts one horizontal row on the bottom.
        return remove_bottom_border(img[:-1])

    else:
        return img

def remove_left_border(img):
    if (img[:, 0] <= max_color).all():
        # Cuts one vertical row on the left.
        return remove_left_border(img[:, 1:])

    else:
        return img

def remove_right_border(img):
    if (img[:, -1] <= max_color).all():
        # Cuts one vertical row on the right.
        return remove_right_border(img[:, :-1])

    else:
        return img

# END BORDER REMOVAL METHODS



if __name__ == '__main__':
    main()
