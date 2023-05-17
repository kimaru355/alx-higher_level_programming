#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        my_string_copy = ""
        for a in my_string:
            if a == 'c' or a == 'C':
                continue
            my_string_copy += a
        return my_string_copy
