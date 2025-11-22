#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
'''Add 2 tuples.
If a tuple is smaller than 2, use the value 0 for each missing integer.
If a tuple is bigger than 2, use only the first 2 integers.
'''
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    sum1 = a[0] + b[0]
    sum2 = a[1] + b[1]
    return(sum1, sum2)
