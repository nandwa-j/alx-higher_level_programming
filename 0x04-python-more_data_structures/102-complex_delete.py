#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for values in list_keys:
        if value == a_dictionary.get(values):
            del a_dictionary[values]
    return a_dictionary
