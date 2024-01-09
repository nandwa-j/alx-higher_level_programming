#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence !== '':
        new = sentence[0]
    else:
        new = None

    return (len(sentence), new)
