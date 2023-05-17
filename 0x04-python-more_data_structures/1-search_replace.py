#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if my_list == []:
        return new_list
    for i in range(len(my_list)):
        if my_list[i] == search:
            del new_list[i]
            new_list.insert(i, replace)
    return new_list
