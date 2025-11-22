#!/usr/bin/python3
def element_at(my_list, idx):
    if ((idx < 0)):
        return None
    elif ((idx >= len(my_list))):
        return None
    else:
        return my_list[idx]
''' This code will retrieves an element from the list 
If idx is negative or out of range the function will return None'''
