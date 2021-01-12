from Cimpl import *
import random

def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x, y, (r, g, b) in image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        row_and_column_are_in_bounds = False 
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = random.randint(-10, 11)
            rand2 = random.randint(-10, 11)
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = rand1
            random_row = rand2  
            
            # Determine if the random coordinates are in bounds.

            if not random_column in range(get_height) and random_row in range(get_width):
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        col = get_color(image, random_column, random_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, col)
                    
    # Return the scattered image.
    return new_image