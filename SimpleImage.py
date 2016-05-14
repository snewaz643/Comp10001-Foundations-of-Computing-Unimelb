################################################################################
#
# Description:
#
# This module implements a simple interface to reading and writing digital
# images in a variety of standard formats. It is built on top of the Python
# Imaging Library (PIL) http://www.pythonware.com/products/pil/. The main
# purpose of the module is to help students of The University of Melbourne
# subject COMP10001 "Foundations of Computing" with their project for
# edge detection of images. Images are represented as rectangular
# lists of lists of integers, where each pixel is a grey-scale intensity i
# in the range 0 <= i <= 255.
#
# Authors:
#
# Bernie Pope (bjpope@unimelb.edu.au)
#
# Date created:
#
# 29 July 2012
#
# Date modified and reason:
#
# 1 August 2012: converted all input image formats to "L" 8 bit / pixel.
# 5 August 2012: module comments added. 
# 8 August 2014: updated module header comments to reflect usage in 2014
#
################################################################################

from PIL import Image

def read_image(filename):
    """read_image(filename) -> list of lists of pixel intensities
    
    Output image is rectangular, grey-scale, 8 bits per pixel,
    in row major coordinates.
    """
    image = Image.open(filename)
    # Convert image to 8 bit per pixel grey-scale
    # if it is not already in that format.
    if image.mode != 'L':
        image = image.convert('L')
    assert(image.mode == 'L')
    pixels = list(image.getdata())
    # Convert the flat representation into a list of rows.
    width, height = image.size
    rows_cols = []
    for row in range(height):
        this_row = []
        row_offset = row * width
        for col in range(width):
            this_row.append(pixels[row_offset + col])
        rows_cols.append(this_row)
    return rows_cols

def write_image(image, filename):
    """write_image(image, filename) -> None

    Writes image data file to filename.

    Input image must be rectangular, grey-scale, 8 bits per pixel,
    in row major coordinates.
    """
    flat_pixels = []
    for row in image:
        flat_pixels += row
    out_image = Image.new('L', (get_width(image), get_height(image)))
    out_image.putdata(flat_pixels)
    out_image.save(filename)

def get_width(image):
    """get_width(image) -> integer width of the image (number of columns).

    Input image must be rectangular list of lists. The width is
    taken to be the length of the first row of pixels. If the image is
    empty, then the width is defined to be 0.
    """
    if len(image) == 0:
        return 0
    else:
        return len(image[0])

def get_height(image):
    """get_height(image) -> integer height of the image (number of rows).

    Input image must be rectangular list of lists. The height is
    taken to be the number of rows.
    """
    return len(image)

