#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_keys = list(sorted(a_dictionary.keys()))
    for i in sort_keys:
        print('{}: {}'.format(i, a_dictionary.get(i)))
