#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_3 = []
    if set_1 == [] or set_2 == []:
        return set_3
    for i in set_1:
        for j in set_2:
            if i == j:
                set_3.append(i)
    return set_3
