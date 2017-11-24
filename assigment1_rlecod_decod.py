# rle assignment
# by rsofiac
# for patrick hebron's learning machines class
# at nyu itp
# fall 2017

# input can be any string with characters, no numbers
# output will be an encoded tuple of said string printed as a listed string and then a decoded string of said tuple
# source code https://rosettacode.org/wiki/Run-length_encoding#Python
def encode(input_string):
    #initialize count
    count = 1
    #initialize previous character
    prev = ''
    #initialize list where to list characters
    lst = []

    #iterate through charactes in the string looking for their differences
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                #add the new entry to the list
                lst.append(entry)
            #reset count
            count = 1
            #reset character
            prev = character
        else:
            count += 1
    #catch last character and create final list
    else:
        entry = (character,count)
        lst.append(entry)

    #print the list as a string
    for x in lst:
        print ''.join(map(str,x))

# decode(lst)
    q = ""
    for character, count in lst:
        q += character * count

    print q


encode("jsdgkkkasdiii")
