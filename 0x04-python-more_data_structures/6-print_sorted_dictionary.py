#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_keys = list(sorted(a_dictionary))
    for i in my_keys:
        print(f"{i}: {a_dictionary.get(i)}")
