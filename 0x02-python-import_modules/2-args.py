#!/usr/bin/python3
from sys import argv
if __name__ == "__main__" :
    if len(argv) == 1 :
        print("0 argument.")
    elif len(argv) == 2 :
        print("1 argument:")
        print(f'1: {argv[1]}')
    else :
        i = 1
        print(f'{len(argv) - 1} arguments:')
        for _ in argv[1:] :
            print(f'{i}: {_}')
            i += 1