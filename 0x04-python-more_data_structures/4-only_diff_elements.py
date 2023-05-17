#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_3 = []
    if set_1 == [] and set_2 == []:
        return set_3
    elif set_1 == []:
        set_3 = set_2.copy()
        return set_3
    elif set_2 == []:
        set_3 = set_1.copy()
        return set_3
    else:
        for i in set_1:
            if i in set_2:
                continue
            else:
                set_3.append(i)
        for j in set_2:
            if j in set_1:
                continue
            else:
                set_3.append(j)
        return set_3
