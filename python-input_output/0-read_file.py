#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        f = (f.read()[:-1])
        if f == ' ':
            return
        else:
            print(f)
