#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for i in set_1:
        if not i in set_2:
            new_set.append(i)
    for j in set_2:
        if not j in set_1:
            new_set.append(j)
    return new_set
