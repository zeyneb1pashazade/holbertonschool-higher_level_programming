#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = sys.argv
    b = len(a) - 1
    if b == 0:
        print("0 arguments.")
    elif b == 1:
        print("1 argument:")
    else:
        print(f"{b} arguments:")
    for i in range(1, b + 1):
        print(f"{i}: {a[i]}")
