#!/usr/bin/python3
import sys
argv = sys.argv
count = 0
print("{} arguments:".format(len(argv) - 1))
for i in range(1, len(argv)):
    print("{}:{}".format(i, sys.argv[i]))
