from Cimpl import*
import random


def red_channel(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of image in which the green and blue 
    components of every pixel is set to 0 and the red
    component is unchanged.
    
    >>> img = load_image(choose_file())
    >>> red = red_channel(img)
    >>> show(red)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        col = create_color(r, 0, 0)
        set_color(new_image, x, y, col)
    return new_image


def green_channel(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of image in which the red and blue 
    components of every pixel is set to 0 and the green
    component is unchanged.
    
    >>> img = load_image(choose_file())
    >>> green = green_channel(img)
    >>> show(green)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        col = create_color(0, g, 0)
        set_color(new_image, x, y, col)
    return new_image


def blue_channel(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of image in which the green and red 
    components of every pixel is set to 0 and the blue
    component is unchanged.
    
    >>> img = load_image(choose_file())
    >>> blue = blue_channel(img)
    >>> show(blue)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        col = create_color(0, 0, b)
        set_color(new_image, x, y, col)
    return new_image


def reduce_brightness(image, multiplier):
    """ (Cimpl.Image) & int -> Cimpl.Image
    
    Return a copy of image with the brightness
    reduced by multipier's percentage.
    
    >>> img - load_image(choose_file())
    >>> dark = reduce_brightness(img. 0.5)
    >>> show(dark)
    """
    
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        col = create_color(r * multiplier, g * multiplier, b * multiplier)
        set_color(new_image, x, y, col)
        
    return new_image


def swap_red_blue(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of image with the red
    and blue components switched.
    
    >>> img = load_image(choose_file())
    >>> swap = swap_red_blue(img)
    >>> show(swap)
    """
    
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        col = create_color(b, g, r)
        set_color(new_image, x, y, col)
        
    return new_image


def hide_image(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of image with the red component
    replaced with the average of red, green and blue
    componenets, green and blue components are replaced with
    random ints from 0 to 255
    
    >>> img = load_image(choose_file())
    >>> hide = hide_image(img)
    >>> show(hide)
    """    
    
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        i = random.randint(0, 255)
        col = create_color( ((r + g + b) / 3) / 10, i, i)
        set_color(new_image, x, y, col)
        
    return new_image


def recover_image(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Recovers image after beging hidden.
    
    >>> img = load_image(choose_file())
    >>> hide = hide_image(img)
    >>> recovered = recover_image(hide)
    >>> show(recovered)
    """     
    
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        red = r * 10
        green = (r + g + b) / 30
        blue = (r + g + b) / 30
        col = create_color(red, green, blue)
        set_color(new_image, x, y, col)
        
    return new_image

