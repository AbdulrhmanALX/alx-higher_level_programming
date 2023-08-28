#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return div = a / b
    except (ValueError, ZeroDivisionError, FloatingPointError):
        div =  None
    finally:
        print("Inside result: {}".format(div))
    return div
