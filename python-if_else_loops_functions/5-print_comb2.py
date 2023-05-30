#!/usr/bin/python3
for i in range(0,10):
    for y in range(0,10):
        if i == 9 and y == 9:
            print(f"{i}{y}")
            break;
        print(f"{i}{y}, ",end='')
