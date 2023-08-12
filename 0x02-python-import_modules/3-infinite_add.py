#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    x = 0
    for _ in argv[1:]:
        x += int(_) 
    print(x) 