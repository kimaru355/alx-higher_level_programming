#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list != [] and x != 0:
        a = 0
        for i in my_list:
            print_int(i)
            a += 1
            if a == x:
                break
        print()
        return a
    else:
        print()
        return 0


def print_int(i):
    try:
        print("{:d}".format(i), end="")
    except ValueError:
        print_float(i)


def print_float(i):
    try:
        print("{:f}".format(i).rstrip('0').rstrip('.'), end="")
    except ValueError:
        print_str(i)


def print_str(i):
    try:
        print("{:s}".format(i), end="")
    except ValueError:
        print("", end="")
