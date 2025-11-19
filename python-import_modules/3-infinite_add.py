#!/usr/bin/python3
import sys
if __name__ == "__main__":
    c = 0
    a = sys.argv
    b = len(a) - 1
    for i in range(1, b + 1 ):
        c = c + int(a[i])
    print(c)
