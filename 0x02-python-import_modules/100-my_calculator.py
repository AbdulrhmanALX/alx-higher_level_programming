#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    import calculator_1

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        result = calculator_1.add(a, b)

    elif argv[2] == '-':
        result = calculator_1.sub(a, b)

    elif argv[2] == '*':
        result = calculator_1.mul(a, b)

    elif argv[2] == '/':
        result = calculator_1.div(a, b)

    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print(f'{a} {argv[2]} {b} = {result}')