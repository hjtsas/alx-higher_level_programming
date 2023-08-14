#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    t1 = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    t2 = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    return tuple(map(sum, zip(t1, t2)))
