#!/usr/bin/env python3

import sys
# This program will work by typing
# ./wc.py INPUTFILE

if len(sys.argv) < 2:
    print("Expecting at least one argument on the cmdline")
    print("usage: wc.py INPUT")
    exit()

infile = sys.argv[1]
print("counting lines in file",infile)

num_lines = 0
# your code here, the infile variable will be the name of the first argument
# passed to wc.py script


# open the file

# loop through each line the file
# capture the number of lines in the num_lines variable
# more advanced students can also capture number of total characters
# and number of words

# end the loop

print("{} lines".format(num_lines))
