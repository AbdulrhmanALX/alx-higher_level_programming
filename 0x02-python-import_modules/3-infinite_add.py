#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = 0
    for _ in argv[1:]:
        x += int(_) 
    print(x) 