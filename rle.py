# rle assignment
# by lola
# for patrick hebron's learning machines class
# at nyu itp
# fall 2017

# input can be any string with characters, no numbers
# output will be an encoded string


def coding(input):

    # initialize output
    output = ''

    # initialize counter of same character
    counter = 0

    # count the characters
    countChar = 0

    # initialize current character
    currentChar = input[0]

    # iterate through the input
    for ch in input:

        # add up the countChar
        countChar = countChar + 1

        # check if the character is repeated
        if ch == currentChar:
            counter = counter + 1

        # else, append to the output
        else:
            # append the info
            output = output + currentChar + str(counter)
            # reset counter
            counter = 1
            # reset currentChar
            currentChar = ch

        # catch the last char
        if countChar == len(input):
            output = output + currentChar + str(counter)

    # print output
    print output

def decoding(input):
    print "TODO"
