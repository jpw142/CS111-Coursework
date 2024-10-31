#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def bw(pixels, threshold):
    """ converts an image into black and white determined by brightness threshold """
    new_pixels = create_green_image(len(pixels), len(pixels[0]))
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            b = brightness(pixels[i][j])
            if b > threshold:
                new_pixels[i][j] = [255, 255, 255]
            else:
                new_pixels[i][j] = [0, 0, 0]
    return new_pixels

def upside_down(pixels):
    """ flips a picture upside down """
    new_pixels = create_green_image(len(pixels), len(pixels[0]))
    for i in range(len(pixels) - 1, -1, -1 ):
        for j in range(len(pixels[0])):
            new_pixels[(len(pixels) - 1) - i][j] = pixels[i][j]
    return new_pixels

def reflect(pixels):
    """ reflects a given image """
    new_pixels = create_green_image(len(pixels), len(pixels[0]))
    for i in range(len(pixels)):
        for j in range((len(pixels[0]) + 1)//2 ):
            new_pixels[i][j] = pixels[i][j]
            new_pixels[i][(len(pixels[0]) - 1) - j] = pixels[i][j]
    return new_pixels

def shrink(pixels):
    """ shrinks pixels by a factor of 2 by skipping every other pixel"""
    new_pixels = create_green_image(len(pixels) // 2, len(pixels[0]) // 2)
    for i in range(len(pixels) // 2):
        for j in range(len(pixels[0]) // 2):
            new_pixels[i][j] = pixels[i*2][j*2]
    return new_pixels
