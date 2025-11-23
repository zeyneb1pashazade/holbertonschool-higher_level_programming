#!/usr/bin/python3
def max_integer(my_list=[]):
'''
 Find the biggest integer of a list.
 If the list is empty, function will return None.
'''
    if not my_list:
        return None
    biggest = my_list[0]
    for element in my_list:
        if element > biggest:
            biggest = element
    return biggest
