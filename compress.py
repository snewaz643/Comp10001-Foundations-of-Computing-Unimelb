'''
File Compression

Author: Sarah O'Connor and 
Syed Ahammad Newaz Saif (snewaz@unimelb.edu.au).
    
Student Number:684933    

Summary-This program is used for the iSkynet's database design
that stores large sized information into smaller compact form
that usually saves a lot of storage space.The information contain
all human knowledge, from Wikipedia to top-secret government sources.
My predecessor, Sarah O'Connor had written out the entire code in 
a haphazard way that makes it extremely difficult to read. I have 
tried to analyse and clearly explain the entire software to make it
readable.

The code tries to take a text file of variable length and   
compress it by making subsequent function calls that would at the end
make another text file of the compressed form of the original file.

The program does no error checking.

Example Usage:

    compress_file(2, 'before_compress.txt', 'after_compress')

This will read the text file called before_compress.txt, compress 
files making ngrams of size 2, and write the resulting compressed 
text file to after_compress.

Testing:

    run_tests()

This will run unit tests on various parts of the program
and check the output for correctness.

Revision history:

8  Sep 2014: Ran some testing with the functions individually.
9  Sep 2014: Started writing the module docstring.
10  Sep 2014: Made major modification to the pre existant module 
             docstring
13 Sep 2014: Added comments to the complicated and vital parts of the functions
15 Sep 2014: Written a separate docstrings for each function
16 Sep 2014: Put some Test modules of things I have tested with.
17 Sep 2014: Ran code through pylint, fixed all warnings.

Desirable features to add in the future:
    - Support for large text files .
    - Better compression results and more storage space to be made for
      other purposes.
'''
''' '''
VERSION = 1.0

NUM_BYTES = 256

ALL_BYTES = set()
for byte_val in range(NUM_BYTES):
    ALL_BYTES.add(chr(byte_val))

def get_unused_bytes(string):#done-1
    '''It makes use of the string provided and
    returns unused bytes of that string 
    by using set difference of the string
    
    Examples:
    >>>>>> get_unused_bytes('abracadabra')
    set(['\x00', '\x83', '\x04', '\x87', '\x08',
    '\x8b', '\x0c', '\x8f', '\x10', '\x93', '\x14',
    '\x97', '\x18', '\x9b', '\x1c', '\x9f', ' ', 
    '\xa3', '$', '\xa7',     '(', '\xab', ',', '\xaf',
    '0', '\xb3', '4', '\xb7', '8', '\xbb', '<', '\xbf',
    '@', '\xc3', 'D', '\xc7', 'H', '\xcb', 'L', '\xcf',
    'P', '\xd3', 'T', '\xd7',       'X', '\xdb', '\\', 
    '\xdf', '`', '\xe3', '\xe7', 'h', '\xeb', 'l', '\xef',
    'p', '\xf3', 't', '\xf7', 'x', '\xfb', '|', '\xff', 
    '\x80', '\x03', '\x84', '\x07',     '\x88', '\x0b', '\x8c',
    '\x0f', '\x90', '\x13', '\x94', '\x17', '\x98', '\x1b',
    '\x9c', '\x1f', '\xa0', '#', '\xa4', "'", '\xa8', '+',
    '\xac', '/', '\xb0',       '3', '\xb4', '7', '\xb8',
    ';', '\xbc', '?', '\xc0', 'C', '\xc4', 'G', '\xc8',
    'K', '\xcc', 'O', '\xd0', 'S', '\xd4', 'W', '\xd8',
    '[', '\xdc', '_', '\xe0',       '\xe4', 'g', '\xe8', 
    'k', '\xec', 'o', '\xf0', 's', '\xf4', 'w', '\xf8', 
    '{', '\xfc', '\x7f', '\x81', '\x02', '\x85', '\x06', 
    '\x89', '\n', '\x8d', '\x0e',       '\x91', '\x12', 
    '\x95', '\x16', '\x99', '\x1a', '\x9d', '\x1e', 
    '\xa1', '"', '\xa5', '&', '\xa9', '*', '\xad', '.', 
    '\xb1', '2', '\xb5', '6', '\xb9', ':','\xbd', '>',
    '\xc1', 'B', '\xc5', 'F', '\xc9', 'J', '\xcd', 'N', 
    '\xd1', 'R', '\xd5', 'V', '\xd9', 'Z', '\xdd', '^',
    '\xe1', '\xe5', 'f', '\xe9', 'j', '\xed',     'n', 
    '\xf1', '\xf5', 'v', '\xf9', 'z', '\xfd', '~', '\x01', 
    '\x82', '\x05', '\x86', '\t', '\x8a', '\r', '\x8e',
     '\x11', '\x92', '\x15', '\x96', '\x19','\x9a', '\x1d',
     '\x9e', '!', '\xa2', '%', '\xa6', ')', '\xaa', '-', 
    '\xae', '1', '\xb2', '5', '\xb6', '9', '\xba', '=', 
    '\xbe', 'A', '\xc2', 'E', '\xc6', 'I',     '\xca', 
    'M', '\xce', 'Q', '\xd2', 'U', '\xd6', 'Y', '\xda', ']',
     '\xde', '\xe2', 'e', '\xe6', 'i', '\xea', 'm', '\xee', 
    'q', '\xf2', 'u', '\xf6', 'y', '\xfa',     '}', '\xfe'])
    '''
    used_bytes = set(string)
    return ALL_BYTES.difference(used_bytes)

def get_ngrams(string, ngram_size):
    '''It takes up a string and then makes
    substrings of the string by following
    convention illustrated by spec
    
    Example:
    >>> get_ngrams('abracadabra', 2)
    ['ab', 'br', 'ra', 'ac', 'ca', 'ad',
     'da', 'ab', 'br', 'ra']
    '''
    result = []
    #index is adjusted by finding the upper 
    #index
    upper_index = len(string) - ngram_size
    #the slice performed by looping over
    #indexes(getting position) and slicing in a way 
    #that initially starting at position 0 goes on 
    #taking elements as ngram and then starting new 
    #lower index with the predecent upper index  
    for index in range(upper_index + 1):
        next_ngram = string[index:index + ngram_size]
        result.append(next_ngram)
    return result

'''It takes up a string and then processes
it in away that each character along with
its count returns as a dictionary'''
def freqs(seq):
    '''It takes up a string and then processes
    it in away that each character along with
    its count returns as a dictionary
    
    Example:
    >>>freqs(get_ngrams('abracadabra', 2))
    {'ac': 1, 'ab': 2, 'ad': 1, 'ca': 1, 
    'da': 1, 'ra': 2, 'br': 2}
    '''
    counters = {}
    #loops over lists
    for item in seq:
        #if already present increment
        if item in counters:
            counters[item] += 1
        #else start off any new element
        #with 1
        else:
            counters[item] = 1
        #return the full dictionary    
    return counters

def get_second_item(seq):
    '''It returns the second element of 
    string,list,set
    
    Example:
    >>> get_second_item((get_ngrams('abracadabra', 2)))
    'br'
    '''
    #the second key
    return seq[1]

def sorted_ngrams_by_freq(dict):
    '''It takes a dictionary and then appends
     the key of the ascending order of frequency
     of values corresponding to the keys
    
    Example:
    >>> sorted_ngrams_by_freq(freqs
    (get_ngrams('abracadabra', 2)))
    ['ab', 'ra', 'br', 'ac', 'ad', 'ca', 'da']
    '''    
    
    items = dict.items()
    #sorts elements(ngrams) into ascending order of values by
    #using reverse= True of the descending order of values 
    sorted_items = sorted(items, key=get_second_item, reverse=True)
    result = []
    #loop over every key with sorted dictionary
    #and append keys into an empty list
    for ngram, _freq in sorted_items:
        result.append(ngram)
    return result

MAX_MAPPINGS = 255

def make_ngram_encoding(sorted_ngrams, encoding_bytes):
    '''It makes use of the unused bytes in a string and the
    previously sorted ngrams to map ngrams to encoded bytes 
    
    Example:
    >>> make_ngram_encoding(sorted_ngrams_by_freq(freqs
    (get_ngrams('abracadabra', 2))), get_unused_bytes('abracadabra'))
    {'ac': '\x87', 'ab': '\x00', 'ad': '\x08', 'ca': '\x8b', 
    'da': '\x0c', 'ra': '\x83', 'br': '\x04'}
    '''
    result = {}
    count = 0
    #loop over unused bytes n ngrams sorted to map n gram to encoded
    #bytes
    for ngram, encoding_byte in zip(sorted_ngrams, encoding_bytes):
        if count >= MAX_MAPPINGS:
        #does not loop if max maps crossed   
            break
        result[ngram] = encoding_byte
        #map in the form of dictionary 
        count += 1
    return result

def make_header(ngram_size, encoded_ngrams):
    '''
    It sets up the header in the non printable
    string characters using ngram size and the mapping from
    make_ngram_encoding.
    
    Example:
    >>> make_header(2,(make_ngram_encoding
    (sorted_ngrams_by_freq(freqs(get_ngrams
    ('abracadabra', 2))), get_unused_bytes('abracadabra'))))
    '\x07\x02ac\x87ab\x00ad\x08ca\x8bda\x0cra\x83br\x04'
    '''
    #first two bytes constructed by non printable char
    #denoting first number of mappings(string form) 
    #appended with size of ngram used(string form)
    number_mappings = len(encoded_ngrams)
    number_mappings_as_char = chr(number_mappings)
    ngram_size_as_char = chr(ngram_size)
    result = number_mappings_as_char + ngram_size_as_char
    #the sorted ngram from previous function each appended 
    #then one by one (string + non printable char form) to
    #make header
    for ngram in encoded_ngrams:
        result += ngram + encoded_ngrams[ngram]
    return result

def make_encoded_string(string, ngram_size, encoded_ngrams):
    '''
    This function tries to make an encoded string of the
    previously done ngram encoding , string input and a
    ngram size specified to replace ngrams with the corresponding
    hexadecimal value(compared from the make_ngram_encoding) 
    to make it encoded hexadecimal string. 
    
    Example:
    >>> make_encoded_string('abracadabra', 2, (make_ngram_encoding
    (sorted_ngrams_by_freq(freqs(get_ngrams('abracadabra', 2))), 
    get_unused_bytes('abracadabra'))))
    '\x00\x83\x8b\x0c\x04a'
    '''
    
    result  = ''
    index = 0
    #loop over picking up ngrams 
    while index < len(string):
        ngram = string[index:index + ngram_size]
        #check if ngram present and make the list
        if ngram in encoded_ngrams:
            result += encoded_ngrams[ngram]
            index += ngram_size
        #else add the string to result and continue
        else:
            result += string[index]
            index += 1
    return result

MINIMUM_ENCODING_BYTES = 1

def compress_file(ngram_size, in_filename, out_filename):
    '''
    It utilizes all the previous functions taking mapping 
    and corresponds to hexadecimal compressed form of the 
    original text file into a compressed text file
    
    >>>compress_file(2, 'before_compress', 'after_compress')
    It then makes a compress text file called after_compress.
    '''    
    #check made to ensure ngram size is made greater
    #than zero
    if ngram_size <= 0:
        print("n-gram size must be greater than 0")
        return
    
    #works if check is perfect! 
    in_file = open(in_filename)
    contents = in_file.read()
    in_file.close()

    #checks to ensure # of encoding bytes is more than
    #1 to ensure compression
    encoding_bytes = list(get_unused_bytes(contents))
    num_encoding_bytes = len(encoding_bytes)

    if num_encoding_bytes <= MINIMUM_ENCODING_BYTES:
        print("Cannot compress file %s" % in_filename)
        print("Insufficient unused bytes in file")
        print("Found %s unused bytes, but %s are required" %
                 (num_encoding_bytes, MINIMUM_ENCODING_BYTES))
        return

    #final check to ensure at least 1 ngram is present
    ngrams = get_ngrams(contents, ngram_size)
    num_ngrams = len(ngrams)

    if num_ngrams == 0:
        print("Cannot compress file %s" % in_filename)
        print("Zero ngrams found, perhaps file is too small?")
        return

    #subsequent function calls to write out the file thus 
    #compressing it
    #necessary functions calls made then fed to write the 
    #files and then the entire file that has been written
    #is closed
    
    ngram_freqs = freqs(ngrams)
    sorted_ngrams = sorted_ngrams_by_freq(ngram_freqs) 
    encoded_ngrams = make_ngram_encoding(sorted_ngrams, encoding_bytes)
    header = make_header(ngram_size, encoded_ngrams)
    encoded_contents = make_encoded_string(contents, ngram_size,
                           encoded_ngrams)

    out_file = open(out_filename, 'w')
    out_file.write(header)
    out_file.write(encoded_contents)
    out_file.close()

'''In this part I have made all the separate functions that
   would separately call the functions and print them as 
   output,categorizing them in the same order as the functions 
   itself and that usely act as test case for every function 
   over a series of input datas to check the validity of 
   output data,arranged in the following order-
   
   1.get_unused_bytes(string)
   2.get_ngrams(string, ngram_size)
   3.freqs(seq)
   4.get_second_item(seq)
   5.sorted_ngrams_by_freq(dict)
   6.make_ngram_encoding(sorted_ngrams, encoding_bytes)
   7.make_header(ngram_size, encoded_ngrams)
   8.make_encoded_string(string, ngram_size, encoded_ngrams)
   9.compress_file(ngram_size, in_filename, out_filename)

   The arguments of the functions are in ascending order'''



def get_unused_bytes_test():
    #test of get_unused_bytes
    file = open("before_compress.txt") 
    contents1 = file.read()
    file.close()
    test1a = contents1
    print get_unused_bytes(test1a)
    
    file = open("moby_dick_chapter1.txt") 
    contents2 = file.read()
    file.close()
    test1b = contents2
    print get_unused_bytes(test1b)
    
    
def get_ngrams_test():  
    #test of get_ngrams
    file = open("before_compress.txt") 
    contents4 = file.read()
    file.close()
    test2a = contents4
    print get_ngrams(test2a, 2)
    
    file = open("moby_dick_chapter1.txt") 
    contents5 = file.read()
    file.close()
    test2b = contents5
    print get_unused_bytes(test2b, 3)
    
    
def freqs_test():
    #test of freqs
    file = open("before_compress.txt") 
    contents7 = file.read()
    file.close()
    test3a = contents7
    print freqs((get_ngrams(test3a,2)))
    
    file = open("moby_dick_chapter1.txt") 
    contents8 = file.read()
    file.close()
    test3b = contents8
    print freqs((get_ngrams(test3b,3)))
    
          
def get_second_item_test():    
    #test of get_second_item
    file = open("before_compress.txt") 
    contents10 = file.read()
    file.close()
    test4a = contents10
    print get_second_item(get_ngrams(test4a, 2))
    
    file = open("moby_dick_chapter1.txt") 
    contents11 = file.read()
    file.close()
    test4b = contents11
    print get_second_item(get_ngrams(test4b, 2))
    
    
def sorted_ngrams_by_freq_test():    
    #test of sorted_ngrams_by_freq
    file = open("before_compress.txt") 
    contents14 = file.read()
    file.close()
    test5a = contents14
    print sorted_ngrams_by_freq(freqs(get_ngrams(test5a,2)))
    
    file = open("moby_dick_chapter1.txt") 
    contents15 = file.read()
    file.close()
    test5b = contents15
    print sorted_ngrams_by_freq(freqs(get_ngrams(test5b,2)))
    
    
def make_ngram_encoding_test():
    #test of make_ngram_encoding
    file = open("before_compress.txt") 
    contents17 = file.read()
    file.close()
    test6a = contents17
    print make_ngram_encoding\
    (sorted_ngrams_by_freq(freqs\
    (get_ngrams(test6a, 2))),get_unused_bytes(test6a))  
               
    file = open("moby_dick_chapter1.txt") 
    contents18 = file.read()
    file.close()
    test6b = contents18
    print make_ngram_encoding\
    (sorted_ngrams_by_freq(freqs\
    (get_ngrams(test6b,2))),get_unused_bytes(test6b)) 
    
    
def make_header_test(): 
    #test of make_header
    file = open("before_compress.txt") 
    contents20 = file.read()
    file.close()
    test7a = contents20
    print make_header(2, make_ngram_encoding\
    (sorted_ngrams_by_freq(freqs\
    (get_ngrams(test7a, 2))),get_unused_bytes(test7a)))
    
    file = open("moby_dick_chapter1.txt") 
    contents21 = file.read()
    file.close()
    test7b = contents21
    print make_header(2, make_ngram_encoding\
    (sorted_ngrams_by_freq(freqs\
    (get_ngrams(test7b, 2))),get_unused_bytes(test7b)))
    
    
def make_encoded_string_test():
    #test of encoded_string
    file = open("before_compress.txt") 
    contents23 = file.read()
    file.close()
    test8a = contents23
    print make_encoded_string(test8a, 2,make_ngram_encoding\
    (sorted_ngrams_by_freq(freqs\
    (get_ngrams(test8a, 2))),get_unused_bytes(test8a)))
    
    file = open("moby_dick_chapter1.txt") 
    contents23 = file.read()
    file.close()
    test8b = contents23
    print make_encoded_string(test8b, 2, make_ngram_encoding\
    (sorted_ngrams_by_freq(freqs\
    (get_ngrams(test8b, 2))),get_unused_bytes(test8b)))
    
    
def compress_file_test():
    #test of compress_file
    file = open("before_compress.txt") 
    contents25 = file.read()
    file.close()
    test1a = contents25
    print compress_file(2, "before_compress.txt", "after_compress")
    
    file = open("moby_dick_chapter1.txt") 
    contents26 = file.read()
    file.close()
    test1a = contents26
    print compress_file(2, "moby_dick_chapter1.txt", "moby_compress")
    