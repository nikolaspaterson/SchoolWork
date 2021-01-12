""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""

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

def extreme_contrast(image): #Fix me
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
        
def sepia_tint(image): #Fix me
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