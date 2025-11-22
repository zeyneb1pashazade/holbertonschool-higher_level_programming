#!/usr/bin/python3
def new_in_list(my_list, idx, element):
'''Replace an element in a list at a specific position without modifying the original list.
If idx is negative or out of range the function will return a copy of the original list
'''
    list = my_list[:]
    if ((idx < 0)) or ((idx >= len(my_list))):
        return list
    else:
        list[idx] = element
        return list
        return my_list
