import math
"""
SYSC 1005 Fall 2018 Lab 9, Parts 2 and 3
"""

def get_points():
    """ (None) -> set of 2-tuples of float
    
    Return a set of (x, y) points, with each point stored in a tuple.
    
    >>> get_points()
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

def fit_line_to_points(points):
    sumx = 0
    sumy = 0
    sumxx = 0
    sumxy = 0
    for (x, y) in points:
        sumx += x
        sumy += y
        sumxx += (x * x)
        sumxy += (x * y)
    m = (sumx * sumy - len(points) * sumxy) / (sumx * sumx - len(points) * sumxx) 
    b = (sumx * sumxy-sumxx * sumy) / (sumx * sumx - len(points) * sumxx)
    
    if(b >= 0):
        return "y = " + str(m) + "x + " + str(b)
    else:
        return "y = " + str(m) + "x - " + str(math.fabs(b))

def read_and_print_lines():
    infile = open('data.txt', 'r')
    for line in infile:
        print(line)
    infile.close()
    
def read_points(filename):
    infile = open(filename, 'r')
    s = set()
    for line in infile:
        p = line.split()
        x = float(p[0])
        y = float(p[1])
        point = (x, y)
        s.add(point)
    infile.close()
    return s
    


if __name__ == "__main__":
    print("The best-fit line is " + fit_line_to_points(get_points()))
    #print(fit_line_to_points(read_and_print_lines()
    command = input("Enter File name ")
    print(fit_line_to_points(read_points(command)))
    