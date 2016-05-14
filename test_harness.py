'''
Test harness for COMP10001 Foundations of Computing
Project 2, Semester 2 2014.

The purpose of this module is to help students in COMP10001 test whether their
decompression program works as expected.

Author: Bernie Pope (bjpope@unimelb.edu.au)

It can be used like so:

>>> from test_harness import round_trip
>>> round_trip(2, "moby_dick_chapter1.txt", "moby_compress", "moby_decompress")
True
>>> round_trip(3, "moby_dick_chapter1.txt", "moby_compress", "moby_decompress")
True
>>> round_trip(4, "moby_dick_chapter1.txt", "moby_compress", "moby_decompress")
True

Revision History:

6 Sep 2014: Initial version for project specification.
'''

from compress import compress_file

from decompress import decompress_file


def round_trip(ngram_size, before_compress, after_compress, after_decompress):
    """Compress an input file, decompress it, and then compare the
    contents of the original file to the decompressed result. If they are
    exactly the same return True otherwise return False.

    Arguments:

    ngram_size: (integer)
        the length of n-grams for compression

    before_compress: (string)
        the name of the original uncompressed file

    after_compress: (string)
        the name of the file to save the compressed output

    after_decompress: (string)
        the name of the file to save the decompressed output.

    Warning: this function will create two new files based on the parameters
    after_compress and after_decompress. It does not check whether those
    files already exist. If they do already exist it will overwrite them,
    losing the old contents.
    """
    # Read the entire contents of the original uncompressed file
    original_file = open(before_compress)
    original_contents = original_file.read()
    original_file.close()
    # Compress the original file and save the result in after_compress
    compress_file(ngram_size, before_compress, after_compress)
    # Decompress the compressed file and save the result in after_decompress
    decompress_file(after_compress, after_decompress)
    # Read the entire contents of the decompressed file
    new_file = open(after_decompress)
    new_contents = new_file.read()
    new_file.close()
    # Return True if the original contents is exactly the same as the
    # decompressed contents, and False otherwise
    return original_contents == new_contents