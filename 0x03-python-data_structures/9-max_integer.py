#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    biggest = -999999
    for i in my_list:
        if i > biggest:
            biggest = i
    return biggest
