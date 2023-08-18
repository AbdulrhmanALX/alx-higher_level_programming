#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    if not matrix:
        print()
    else:
        for row in matrix:
            for col in row:
                if row.index(col) == len(row) - 1:
                    print("{:d}".format(col), end="")
                else:
                    print("{:d}".format(col), end=" ")
            print()
