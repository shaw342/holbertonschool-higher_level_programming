#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return len(sentence), None
    a = len(sentence)
    return a, sentence[0]
