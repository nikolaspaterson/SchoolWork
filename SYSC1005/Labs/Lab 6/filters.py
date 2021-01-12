""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""
import math
from Cimpl import *

def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def weighted_grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a weighted grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> weight_gray_image = weighted_grayscale(image)
    >>> show(weight_gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        
        brightness = r * 0.299 + g * 0.587 + b * 0.114
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def extreme_contrast(image): 
    """ (Cimple.Image) -> Cimpl.Image
    
    Return a copy of image, maximizing the contrast between
    the light and dark pixels.
    
    >>> image = load_image(choose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        
        if r < 128:
            red = 0
        else:
            red = 255
            
        if g < 128:
            green = 0
        else:
            green = 255
            
        if b < 128:
            blue = 0
        else:
            blue = 255

        contrast = create_color(red, green, blue)
        set_color(new_image, x, y, contrast)
        
    return new_image
        
def sepia_tint(image): 
    """ (Cimple.Image) -> Cimpl.Image
    
    Return a copy of image in which the colors have been
    converted to sepia tones.
    
    >>> image = load_image(choose_file())
    >>> new_image = sepia_tint(image)
    >>> show(new_image)
    """
    new_image = weighted_grayscale(image)
    
    for x, y, (r, g, b) in new_image:
        if r < 63:
            red = r * 1.1
            blue = b * 0.9
        elif r > 191:
            red = r * 1.08
            blue = b * 0.93
        else:
            red = r * 1.15
            blue = b * 0.85
            
        sepia = create_color(red, g, blue)
        set_color(new_image, x, y, sepia)
    
    return new_image

def _adjust_component(amount):
    """ (int) -> int
    
    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.
   
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    if amount < 64:
        return 31
    elif 63 < amount < 128:
        return 95
    elif 127 < amount < 192:
        return 159
    else:
        return 223
    
def posterize(image): 
    """ (Cimple.Image) -> Cimpl.Image
    
    Return a "posterized" copy of image.
    
    >>> image = load_image(choose_file())
    >>> new_image = posterize(image)
    >>> show(new_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        
        red = _adjust_component(r)
        green = _adjust_component(g) 
        blue = _adjust_component(b)
        
        col = create_color(red, green, blue)
        set_color(new_image, x, y, col)
        
    return new_image

def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image
    
    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image)):
            
            r1, g1, b1 = get_color(image, x, y)
            r2, g2, b2 = get_color(image, x, y + 1)
            
            if(abs((r1 + g1 + b1) / 3 - (r2 + g2 + b2) / 3) > threshold):
                set_color(new_image, x, y, black)
                
            else:
                set_color(new_image, x, y, white)
                
    return new_image

def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image
    
    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    
    >>> filtered = detect_edges_better(image, 10.0)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image) - 1):
            
            r1, g1, b1 = get_color(image, x, y)
            r2, g2, b2 = get_color(image, x, y + 1) #BELOW
            r3, g3, b3 = get_color(image, x + 1, y) #RIGHT
            
            if(abs((r1 + g1 + b1) / 3 - (r2 + g2 + b2) / 3) > threshold):
                set_color(new_image, x, y, black)
                
            elif(abs((r1 + g1 + b1) / 3 - (r3 + g3 + b3) / 3) > threshold):
                set_color(new_image, x, y, black)
                
            else:
                set_color(new_image, x, y, white)
    
    return new_image

def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # When generating the pixel coordinates, we have to ensure that (x, y)
    # is never the location of pixel on the top, bottom, left or right edges
    # of the image, because those pixels don't have four neighbours.
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(image)):
    #     for x in range(0, get_width(image)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            l_top_r, l_top_g, l_top_b = get_color(image, x - 1, y - 1)
            r_top_r, r_top_g, r_top_b = get_color(image, x + 1, y - 1)
            l_bot_r, l_bot_g, l_bot_b = get_color(image, x - 1, y + 1)
            r_bot_r, r_bot_g, r_bot_b = get_color(image, x + 1, y + 1)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + l_top_r + r_top_r +
                       l_bot_r + r_bot_r ) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green + l_top_g +
                                   r_top_g +l_bot_g + r_bot_g ) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue + l_top_b + 
                                   r_top_b + l_bot_b + r_bot_b) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target

def flip_vertical(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return an image that contains a copy of the original image
    after it has been flipped around an imaginary vertical line
    drawn through its midpoint.
    
    >>> image = load_image(choose_file())
    >>> filtered = flip_vertical(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range(0, get_height(image)):
        for x in range(0, get_width(image)):
            w = get_width(image) - 1 - x
            #h = get_height(image) - 1 - y this flips it horizontally
            r, g, b = get_color(image, w, y)
            col = create_color(r,g,b)
            set_color(new_image, x, y, col)
    return new_image