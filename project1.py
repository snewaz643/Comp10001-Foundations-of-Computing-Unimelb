'''
Skeleton Python file for COMP10001 project 1.
Edge detection.

Name-Syed Ahammad Newaz Saif 

Student number 684933 .

Description:The intention of this program is to make an output 
images with edges that has a large scale applications as in
robotics,artifical intelligence(my favourite part),forensics
and many other science and non-science branches. A particular
dimension of greyscale image provided as input which could be in the
form of .jpg,.png or any type of images.The function actually
starts of detecting the pixels of the image and then converts the
pixels into a lists of lists access the elements within 
the and converts the elements with comparison to a
threshold and makes a new list of list that combines
to form a new image with edges of the input images.
Edges are produced in places where there is a change
in pixel intensities.

Development of code with  important dates:

15-08-14:Initally started working in the functions individually
that lead to very complex handling elements in list of list

21-08-14:Started eliminating chunks of complicated parts upto
first two functions

23-08-14:Then started to work on third and fourth functions
trying to make it in best simplified form

25-08-14:Worked on the last functions but got lists instead
of list of lists that would not produce white edgy lines

29-08-14:I came up with a solution to output out lists 
of list but still not only few edges were visible

02-09-14:Starting summarizing using comments on the sides 
of the major bodies of the individual functions present

03-09-14:Lastly ended up with a solution that perfectly
produces the edge and well-styled codes

04-09-14:Last touches to finishing the project

11 Aug 2014: Initial skeleton file. Version 1. Provided by Bernie Pope.
'''

from SimpleImage import (get_height, get_width, read_image, write_image)

from math import sqrt 

def gradient_row(image, row, col):
    
    '''This function accesses out and in of range 
    elements(rowwise->column wise),maintains line 
    length.

    This function was provided in the project
    specification.

    Examples:
    
    >>> gradient_row(CHECKER, 0, 0)
    -37
    >>> gradient_row(CHECKER, 5, 2)
    -885
    >>> gradient_row(CHECKER, 7, 5)
    23
    >>> gradient_row(CHECKER, 9, 0)
    -47
    ''' 
    
    #extracts out elements out and in range
    #as spec describes taking invidual 
    #pixels n backslashes handy
    #to maintain line length
    pixel1_row = get_pixel(image, row-1, col-1)
    pixel2_row = + 2*get_pixel(image, row-1, col)
    pixel3_row = + get_pixel(image, row-1, col+1)
    pixel4_row = - get_pixel(image, row+1, col-1)
    pixel5_row = - 2*get_pixel(image, row+1, col)
    pixel6_row = - get_pixel(image, row+1, col+1) 
    result_row = pixel1_row + pixel2_row +\
         pixel3_row + pixel4_row + pixel5_row + pixel6_row
    
    return result_row

def gradient_col(image, row, col):
    
    '''It accesses out and in of range elements
    (columnwise->rowwise)and maintains 
    line length

    This function was provided in the project
    specification.

    Examples:

    >>> gradient_col(CHECKER, 0, 0)
    -27
    >>> gradient_col(CHECKER, 5, 2)
    31
    >>> gradient_col(CHECKER, 7, 5)
    -825
    >>> gradient_col(CHECKER, 9, 0)
    45
    '''
     
    #extracts out elements out n in range
    #as spec describes taking invidual 
    #pixels n backslashes handy
    #to maintain line length
    
    pixel1_col = -get_pixel(image, row-1, col-1)
    pixel2_col = - 2*get_pixel(image, row, col-1)
    pixel3_col = - get_pixel(image, row+1, col-1)
    pixel4_col = + get_pixel(image, row-1, col+1)
    pixel5_col = + 2*get_pixel(image, row, col+1)
    pixel6_col = + get_pixel(image, row+1, col+1) 
    result_col = pixel1_col + pixel2_col + \
    pixel3_col + pixel4_col + pixel5_col + pixel6_col
    return result_col 

def gradient_magnitude(image, row, col):
    '''This function calculates the squareroot 
    of sum of squares of gradient_col and 
    gradient_row
    
    This function was provided in the project
    specification.

    Examples:

    >>> gradient_magnitude(CHECKER, 0, 0)
    45.803929962395145
    >>> gradient_magnitude(CHECKER, 5, 2)
    885.5427714119742
    >>> gradient_magnitude(CHECKER, 7, 5)
    825.3205437888967
    >>> gradient_magnitude(CHECKER, 9, 0)
    65.06919393998976
    '''
    
    #squares separately computated
    #then added
    #result returned as the square root
    #of the sum,variables came handy
    row_sqr = gradient_row(image, row, col)**2
    col_sqr = gradient_col(image, row, col)**2
    result = sqrt(row_sqr + col_sqr)
    return result

def gradient_threshold(image, row, col, threshold):
    '''It checks whether the previous gradient_magnitude
    is above the threshold called in the function

    This function was provided in the project
    specification.

    Examples:
    
    >>> gradient_threshold(CHECKER, 0, 0, 0)
    255
    >>> gradient_threshold(CHECKER, 0, 0, 50)
    0
    >>> gradient_threshold(CHECKER, 5, 2, 200)
    255
    >>> gradient_threshold(CHECKER, 7, 5, 900)
    0
    >>> gradient_threshold(CHECKER, 9, 0, 100)
    0
    '''
    #compares gradient magnitude with threshold
    if gradient_magnitude(image, row, col) > threshold:
        return 255
    else:
        return 0

def convolute(image, threshold):
    
    '''It then tries to loop around the elements 
    from the gradient_threshold call(which is a list of 0s 
    and 255s)and tries to create a list by appending the 
    elements and finally combines the list to produce a new 
    lists of list that resembles output image.

    All intensity values in the output edge image must be 
    either 0 or 255. Yourimplementation of convolute must 
    not modify the input image, instead it must construct 
    a completely new image as output.

    This function was provided in the project
    specification.

    Examples:

    >>> convolute(CHECKER, 200)
    [[0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ],
     [0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ],
     [0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ],
     [0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ],
     [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
     [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
     [0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ],
     [0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ],
     [0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ],
     [0, 0, 0, 0, 255, 255, 0, 0, 0, 0 ]]
    '''
    
    #newly formed image as list of list
    new_image = []
    #first loops over row
    for rrow in range(get_height(image)):
        #collects data (elements of list)
        #to later combine with other data
        #so the pixel produced is later
        #combined with other pixels
        #list appended to list forming image
        new_pixel = []
        #loops over col wise appending elements
        #forming pixels
        for colr in range(get_width(image)):
            #conversion of grayscale image to
            #black n white images of 0 and 255
            #with edges
            y = gradient_threshold(image, rrow, colr, threshold)
            new_pixel.append(y)
        new_image.append(new_pixel)                  
    return new_image

def clamp(val, lower_bound, upper_bound):
    '''Restrict a value to be within the range:

        lower_bound <= val <= upper_bound

    Return val if it is within the range, otherwise
    return the nearest bound to val.

    We assume (but do not check) that
    lower_bound <= upper_bound. The function may
    return the wrong result if this is not satisfied.

    This function was provided in the project
    specification.

    Examples:

    >>> clamp(10, 0, 100)
    10
    >>> clamp(-10, 0, 100)
    0
    >>> clamp(110, 0, 100)
    100
    '''
    return max(min(val, upper_bound), lower_bound)

def get_pixel(image, row, col):
    '''Return the intensity of a pixel in image at
    coordinate (row, col) if that coordinate is
    within the bounds of the image. If the coordinate
    is outside the bounds of the image then return
    the intensity of its nearest in-bounds neighbour.

    image is a list of lists of pixel intensities
    (integers). row and col are integers.

    We assume (but do not check) that the image
    is not empty. An empty input image will result
    in an IndexError.

    This function was provided in the project
    specification.

    Examples:

    >>> example_image = [[1,2,3], [4,5,6]]
    >>> get_pixel(example_image, 0, 0)
    1
    >>> get_pixel(example_image, 0, 1)
    2
    >>> get_pixel(example_image, -1, 0)
    1
    >>> get_pixel(example_image, 1, 3)
    6
    '''
    # Find the bounds of the image.
    max_row = get_height(image) - 1
    max_col = get_width(image) - 1
    # Make sure the coordinate is within the image
    # bounds.
    new_row = clamp(row, 0, max_row)
    new_col = clamp(col, 0, max_col)
    return image[new_row][new_col]

def edge_detect(in_filename, out_filename, threshold):
    '''Apply the edge detection algorithm to an image file
    and save the result to an output file. Gradient scores
    above the threshold parameter are considered edges.

    Example, assuming we have a file called 'floyd.png'
    in the same directory as the program. The output
    will be saved in a file called 'floyd_edge.png':

    in_filename and out_filename are strings. threshold
    is a number (integer or float).

    The result is None.

    >>>edge_detect('floyd.png', 'floyd_edge.png', 200)'''
    
    in_image = read_image(in_filename)
    out_image = convolute(in_image, threshold)
    write_image(out_image, out_filename)

CHECKER = [[11,  1,   2,   15,  35,  247, 205, 240, 214, 219],
           [17,  20,  24,  35,  0,   235, 235, 238, 249, 223],
           [17,  31,  27,  31,  46,  209, 239, 236, 247, 230],
           [12,  1,   37,  24,  38,  241, 219, 220, 231, 211],
           [37,  13,  19,  10,  44,  255, 220, 235, 227, 252],
           [243, 205, 227, 224, 239, 12,  21,  47,  42,  9],
           [220, 241, 234, 237, 223, 50,  16,  0,   1,   28],
           [248, 241, 207, 247, 218, 13,  14,  48,  39,  42],
           [204, 213, 230, 248, 213, 50,  3,   28,  25,  8],
           [215, 227, 249, 226, 254, 40,  11,  35,  48,  45]]

'''In this part I have made all the separate functions that
   would separately call the functions and print them as 
   output,categorizing them in the same order as the functions 
   itself and that usely act as test case for every function 
   over a series of input datas to check the validity of 
   output data,arranged in the following order-
   
   1.gradient_row(image,row,col)
   2.gradient_col(image,row,col)
   3.gradient_magnitude(image,row,col)
   4.gradient_threshold(image,row,col,threshold)
   5.convolute(image,threshold)
   
   The arguments of the functions are in ascending order
 
    ''' 

def gradient_row_test():
    #gradient row tests as per spec sheet
    print gradient_row(CHECKER, 0, 0)
    print gradient_row(CHECKER, 5, 2)
    print gradient_row(CHECKER, 7, 5)
    print gradient_row(CHECKER, 9, 0)

def gradient_col_test():
    #gradient row tests as per spec sheet
    print gradient_col(CHECKER, 0, 0)
    print gradient_col(CHECKER, 5, 2)
    print gradient_col(CHECKER, 7, 5)
    print gradient_col(CHECKER, 9, 0)

def gradient_magnitude_test():
    #gradient magnitude tests as per spec sheet
    print gradient_magnitude(CHECKER, 0, 0)
    print gradient_magnitude(CHECKER, 5, 2)
    print gradient_magnitude(CHECKER, 7, 5)
    print gradient_magnitude(CHECKER, 9, 0)

def gradient_threshold_test():
    #gradient threshold tests as per spec sheet
    print gradient_threshold(CHECKER,0,0,0)
    print gradient_threshold(CHECKER,0,0,50)
    print gradient_threshold(CHECKER,9,0,100)
    print gradient_threshold(CHECKER,5,2,200)
    print gradient_threshold(CHECKER,7,5,900)

def convolute_test():
    #convolute tests as per spec sheet 
    print convolute(CHECKER,50)
    print convolute(CHECKER,100)
    print convolute(CHECKER,200)
    print convolute(CHECKER,400)
    print convolute(CHECKER,900)

def edge_detect_test():
    #edge detect tests as per spec sheet
    print edge_detect('floyd.png', 'floyd_edge.png', 50)
    print edge_detect('floyd.png', 'floyd_edge2.png', 100)
    print edge_detect('floyd.png', 'floyd_edge3.png', 200)
    print edge_detect('floyd.png', 'floyd_edge4.png', 400)
    print edge_detect('floyd.png', 'floyd_edge5.png', 900) 
