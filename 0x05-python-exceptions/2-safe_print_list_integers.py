#!/usr/bin/python3

def safe_print_list_integers(my_list[], x=0):
    if my_list != [] and x != 0:
        a = 0
        b = 0
        for i in my_list:
            a += 1
            try:
                print("{:d}".format(i), end="")
                b += 1
            except ValueError:
                continue
            if i == x:
                break
        return b
