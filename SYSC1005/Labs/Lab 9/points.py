import math
def distance(pt1, pt2):
    """ (2-tuple of float, 2-tuple of float) -> float
    
    Return the distance of the line between 2-D points
    pt1 and pt2.
    
    >>> point1 = (1.0, 2.0)
    >>> point2 = (4.0, 6.0)
    >>> distance(point1, point2)
    5.0
    """
    return math.sqrt(math.pow((pt2[1] - pt1[1]), 2) + math.pow((pt2[0] - pt1[0]), 2))