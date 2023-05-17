#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list == []:
        return 0
    counter = []
    counts = 0
    for i in my_list:
        if i in counter:
            continue
        else:
            counter.append(i)
            counts += i
    return counts
