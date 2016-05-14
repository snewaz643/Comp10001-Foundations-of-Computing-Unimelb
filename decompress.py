'''
File Decompression

Author: Syed Ahammad Newaz Saif (snewaz@unimelb.edu.au).
Student Number:684933    

Summary-Sarah O'Connor,my predecessor made the compression 
software but for mulititue reasons it seems that the 
decompressed files are not available and the iSkynet's database 
needs to check on the files.This program serves to decompress 
out the contents using the previous program that was set up 
by my predecessor.

The whole program works in such a way that for a given text
and its characters unused bytes,referred to as, the encoding bytes 
are used to map non printable compressed text files with respect
to a dictionary file that is being made in this program. The entire
function uses each byte of the compressed text file (hexadecimal form)
to eventually end up with the original file.

The text file is broken into two parts-a.header b.content information
The header file contains information about the dictionary set up to
get the information.First byte contains the number of mappings
and the second byte contains the ngram size.The rest is then repeated
using the combination of ngrams and encoded bytes.The two bytes
work to give the header length 2 + (number_mappings *(ngram_size + 1))
in bytes.The rest is the contents that is found using the header 
details and the certain functions in the program.

The file is then tested over test harness for correctness.

Example Usage:
  >>> from decompress import decompress_file
  >>> decompress_file("after_compress", "after_decompress")
  >>> file = open("after_decompress")
  >>> contents = file.read()
  >>> file.close()
  >>> contents
  abracadabra\n 

This will read the text file called after_compress, decompress its
files and write the resulting decompressed text file to
after_decompress that can be viewed by assigning it to read
and calling it using variable contents.
     
Testing:

    run_tests()

This will run unit tests on various parts of the program
and check the output for correctness.

Revision history:

3  Sep 2014: Implemented the get_header_info 
4  Sep 2014: Implemented the parse_header after analyzing 
its functionality
9  Sep 2014: Implemented the get_compressed_body 
10 Sep 2014: Implemented decompressed_body and 
decompressed_file
11 Sep 2014: Added docstrings and comments to vital
and complicated parts
12 Sep 2014: Added test cases.
16 Sep 2014: Ran code through pylint, fixed all warnings.

Desirable features to add in the future:
    - Improve for larger files.
    - Decompression in less and tidy 
    way with cases that does not use encoding
    bytes
'''
# Importing compress to different conditions
#obtain various compressed_contents set to
#variable to be used for test cases.
from compress import compress_file,get_ngrams,\
get_unused_bytes,sorted_ngrams_by_freq, \
make_ngram_encoding,make_encoded_string, freqs

compress_file(2, "before_compress.txt", "after_compress")
file = open("after_compress")
compressed_contents = file.read()
file.close()

compress_file(2, "moby_dick_chapter1.txt", "moby_compress")
file = open("moby_compress")
compressed_contents1 = file.read()
file.close()


compress_file(2, "moby_dick.txt", "moby_compress1")
file = open("moby_compress1")
compressed_contents2 = file.read()
file.close()



def get_header_info(compressed_contents):
    '''
    This function looks over the contents
    of the compressed file and uses first
    two bytes of the header to determine the
    the number of mappings in the header of
    the compressed contents, and ngram_size 
    is the length of n-grams in the compressed 
    file that is returned as a two-element
    tuple by taking string as input.
    
    Example:
    
    >>> from decompress import get_header_info
    >>> get_header_info(compressed_contents)
    (8, 2)
    '''
    #It has been assumed as the argument string 
    #being at least two bytes long
    if len(compressed_contents) >= 2:
        #ord function helps to turn thenon printable 
        #versions(hexadecimal in most case) to be in their 
        #corresponding numerical form
        num_mappings = ord(compressed_contents[0]) 
        ngram = ord(compressed_contents[1])
    return (num_mappings, ngram)

def parse_header(compressed_contents):
    '''
    This function takes a string as its argument and 
    returns a dictionary as its result. The argument corresponds
    to the contents of a compressed file. The dictionary result 
    represents the mapping in the header of the compressed contents. 
    The keys of the dictionary should be encoding bytes and the values 
    of the dictionary should be n-grams
    
    Example:
    
    >>> from decompress import parse_header
    >>> decode_map = parse_header(compressed_contents)
    >>> decode_map
    {\x00: 'ab', \x83: 'ra', \x04: 'br', \x87: 'ac', 
    \x08: 'ad', \x8b: 'ca', \x0c: 'a\n' , , \x8f: 'da'}
    '''
    decode_map={}
    #finds out the index of the contents using previous function
    num_mappings = get_header_info(compressed_contents)[0] 
    ngram = get_header_info(compressed_contents)[1]
    for index in range(num_mappings):
        #adjustment of the slicing made
        start_pos = 2 + (ngram+1)*index
        end_pos = start_pos + ngram
        #values then keys extracted with hexadecimal values(keys) following 
        #two characters(values denoting ngrams) over the end of the header
        values = compressed_contents[start_pos:end_pos]
        keys = compressed_contents[end_pos]
        #mapping of hexadecimal to corresponding ngrsm
        decode_map[keys]= values

    return decode_map

def get_compressed_body(compressed_contents):        
    '''
    This function takes a string as its argument and returns a string as its result
    The argument corresponds to the contents of a compressed file. 
    The result is the contents of the compressed file that follows 
    immediately after the header.
    
    Example:
    
    >>> from decompress import get_compressed_body
       >>> compressed_body = get_compressed_body(compressed_contents)
       >>> compressed_body
       \x00\x83\x8b\x8f\x04\x0c
    '''
    #slicing technique used in such a way that it starts from the 
    #the 27 th position since header ends at 26th position
    number_mappings = get_header_info(compressed_contents)[0]
    
    n_gram = get_header_info(compressed_contents)[1]
    
    compressed_body = compressed_contents[(2 +((n_gram+1)*number_mappings)):]
     
    return compressed_body
            
def decompress_body(decode_map, compressed_body):
    '''
    This function takes two arguments and returns a string as its result. 
    The first argument is a dictionary which maps encoding bytes to n-grams, 
    it is in the same format as the output of parse_header. The second
    argument is a string representing the body of the compressed file. 
    It is in the same format as the output of get_compressed_body. 
    The output string is a decompressed version of the compressed file. 
    Foreach input byte in compressed_body the function should produce 
    one or more bytes of output. Input bytes that are keys of decode_map 
    should be replaced by their corresponding n-grams (their values in
    decode_map). All other input bytes should be copied directly 
    to the output unchanged.
    
    Example:
    
    >>> from decompress import decompress_body
    >>> decompressed_contents = decompress_body(decode_map, compressed_body)
    >>> decompressed_contents
    abracadabra\n 
    
    By feeding the outputs of parse_header and get_compressed_body 
    to decompress_body we can obtain the original uncompressed 
    contents of the file.
    '''
    new_word = ''
    
    for check in compressed_body:
        if check in (decode_map).keys():
            #check_pos finds out the positions 
            check_pos = decode_map.keys().index(check)
            #the positions are then utilised to dig deep to 
            #find the values everytime
            #the values are then replaced with each non-printable 
            #bytes to get contents that was compressed
            new_word += decode_map.items()[check_pos][1]
        else:
            new_word+= check
            
    return new_word 
    
def decompress_file(in_filename,out_filename):
    '''This function reads in_filename, decompresses
    its contents, writes the decompressed contents to out_filename, 
    and return None as its result. Your decompress_file function 
    will need to call upon (some of) the functions doned in tasks 2 to 5 in
    order to achieve the desired behaviour.Both arguments are strings
    indicating filenames.
    
    Example:
    
    >>> from decompress import decompress_file
    >>> decompress_file("after_compress", "after_decompress")
    >>> file = open("after_decompress")
    >>> contents = file.read()
    >>> file.close()
    >>> contents
    abracadabra\n 
    
    At the end of this function the after_decompress
    and before_compress should contain the exact same contents 
    that can be confirmed using test_harness.py module provided
    
    Example:
    >>> from test_harness import round_trip
    >>> round_trip(2, "before_compress.txt", "after_compress",
    "moby_decompress")
    True
    >>> round_trip(2, "moby_dick_chapter1.txt", "moby_compress",
    "moby_decompress")
    True
    
    It contains a function called round_trip which compresses 
    an input file, decompresses it, and then compares the contents 
    of the original file to the decompressed result. If they are exactly 
    the same it returns True otherwise it returns False. The first argument 
    is an integer which does the n-gram size for compression. The second 
    argument is a string naming the original file. The third argument is a 
    string naming the file to save the compressed output. The fourth 
    argument is a string naming file to save the decompressed output.'''
    
    #open, read and then close the compressed file
    file = open(in_filename)
    compressed_materials = file.read()
    file.close()
    #the functions 2,3,4 utilized
    #to make the file writing and then
    #closed and None returned
    x = parse_header(compressed_materials)
    y = get_compressed_body(compressed_materials)
    z = decompress_body(x,y)
    file = open(out_filename,'w')
    file.write(z)
    file.close()

'''In this part I have made all the separate functions that
   would separately call the functions and print them as 
   output,categorizing them in the same order as the functions 
   itself and that usely act as test case for every function 
   over a series of input datas to check the validity of 
   output data,arranged in the following order-
   
   1.get_header_info(compressed_contents)
   2.parse_header(compressed_contents)
   3.get_compressed_body(compressed_contents)
   4.decompress_body(decode_map, compressed_body)
   5.decompress_file(in_filename,out_filename)

   The arguments of the functions are in ascending order'''     

def get_header_info_test():
    #test of get_header_info
    print get_header_info(compressed_contents)     
    print get_header_info(compressed_contents1)
    print get_header_info(compressed_contents2)
    
    
def parse_header_test():
    #test of parse_header
    print parse_header(compressed_contents)
    print parse_header(compressed_contents1)
    print parse_header(compressed_contents2)
    
        
        
def get_compressed_body_test():
    #test of get_compressed_body
    print get_compressed_body(compressed_contents)
    print get_compressed_body(compressed_contents1)
    print get_compressed_body(compressed_contents2)
            
    
def decompress_body_test():
    #test of decompress_body
    z2 = get_compressed_body(compressed_contents)
    z1 = parse_header(compressed_contents)
    print decompress_body(z1, z2)
    
    z4 = get_compressed_body(compressed_contents1)
    z3 = parse_header(compressed_contents1)
    print decompress_body(z3, z4)
    
    z6 = get_compressed_body(compressed_contents2)
    z5 = parse_header(compressed_contents2)
    print decompress_body(z5, z6)
    
    
    
def decompress_file_test():
    #test of decompress_file
    from decompress import decompress_file
    z2 = get_compressed_body(compressed_contents)
    z1 = parse_header(compressed_contents)
    after_decompress = decompress_body(z1, z2)
    print decompress_file("after_compress", "after_decompress")
    
    
    z3 = get_compressed_body(compressed_contents1)
    z4 = parse_header(compressed_contents1)
    moby_decompress = decompress_body(z4, z3)
    print decompress_file("moby_compress","moby_decompress")
    
    z6 = get_compressed_body(compressed_contents2)
    z5 = parse_header(compressed_contents2)
    moby_decompress1 = decompress_body(z5, z6)
    print decompress_file("moby_compress1","moby_decompress1")
    
'''In this part I have tried to see the correctness of 
   my code over a series of test cases that basically checks
   if contents of before compression and the after compression
                     "after_decompress")
    print round_trip(2, "moby_dick_chapter1.txt", "moby_compress",\
   are same or not.Testing is done over various sizes of
   files.It relies on functionality of compress.py that 
   first compresses it'''    

def round_trip_test():
    from test_harness import round_trip
    print round_trip(2, "before_compress.txt", "after_compress",\
                      "moby_decompress")
    print round_trip(3, "moby_dick.txt", "moby_compress1",\
                      "moby_decompress1")
    
    