#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if idx < 0:
        return my_list_copy
    elif idx >= len(my_list):
        return my_list_copy
    if my_list:
        del my_list_copy[idx]
        my_list_copy.insert(idx, element)
        return my_list_copy
