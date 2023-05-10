#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if a == 8 and b == 9:
            print(a, b, sep="")
        elif b > a:
            print(a, b, sep="", end=", ")
