#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()
