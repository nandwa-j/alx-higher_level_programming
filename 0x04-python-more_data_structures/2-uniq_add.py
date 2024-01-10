#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    number = 0
    for i in unique:
        number += i

    return number
