#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1]
list_result = divisible_by_2(my_list)

i = 0
print(f"new {len(list_result)} old {len(my_list)}")
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
