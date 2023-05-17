#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = 1
    b = 2
    c = 1
    d = 2
    if len(tuple_a) < 1:
        a = 0
        b = 0
    elif len(tuple_a) < 2:
        b = 0
    if len(tuple_b) < 1:
        c = 0
        d = 0
    elif len(tuple_b) < 2:
        d = 0
    if a != 0:
        a = tuple_a[0]
    if b != 0:
        b = tuple_a[1]
    if c != 0:
        c = tuple_b[0]
    if d != 0:
        d = tuple_b[1]
    tuple_c = (a+c, b+d)
    return tuple_c
