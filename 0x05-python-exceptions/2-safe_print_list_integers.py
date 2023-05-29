#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if my_list != [] and x != 0:
        a = 0
        b = 0
        for i in range(0, x):
            a += 1
            try:
                print("{:d}".format(my_list[i]), end="")
                b += 1
            except ValueError:
                continue
            except TypeError:
                continue
            if a == x:
                break
        print()
        return b
