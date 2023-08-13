#!/usr/bin/python3

def no_c(my_string):

    for char in my_string:
        if char not in "cC":
            new_string = [x for x in my_string if x != 'cC']
            return ("".join(new_string))
