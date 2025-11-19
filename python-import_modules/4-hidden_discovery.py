#!/usr/bin/python3
import  hidden_4
if __name__ == "__main__":
    a = dir(hidden_4)
    for i in sorted(a):
        if i[0] != "_":
            print(i, end = "\n")
