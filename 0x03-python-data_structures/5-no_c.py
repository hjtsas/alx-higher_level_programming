#!/usr/bin/python3

def no_c(my_string):

    for char in my_string:
        new_string = [x for x in my_string if x != 'C' and x != 'c']
        return ("".join(new_string))
