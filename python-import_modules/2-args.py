#!/usr/bin/python3
import sys
argv = sys.argv
if (len(argv) - 1) == 1:
    print("{} argument".format(len(argv) - 1))
else:
    print("{} arguments:".format(len(argv) - 1))
for i in range(1, len(argv)):
    print("{}: {}".format(i, sys.argv[i]))
