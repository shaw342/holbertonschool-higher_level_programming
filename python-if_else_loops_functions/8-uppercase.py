#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            b = ord(i)
            a = chr(b - 32)
            print("{}".format(a), end="")
    print("")
