#!/usr/bin/python3

def multiple_returns(sentence):

    if (len(sentence) - 1) == 0:
        return None
    print('Length: {:d} - First character: {}'.format((len(sentence)-1), sentence[:0]))
