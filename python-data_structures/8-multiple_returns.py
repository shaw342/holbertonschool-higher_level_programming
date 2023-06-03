#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        sentence[0] = None
    a = len(sentence)
    return a,sentence[0]
