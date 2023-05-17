#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        print()
        return None
    my_keys = list(sorted(a_dictionary))
    for i in my_keys:
        print(f"{i}: {a_dictionary.get(i)}")
