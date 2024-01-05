#!/usr/bin/python3
if __name__ =="__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    count_arg = len(argv)
    if count_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[1]
    b = int(argv[3])
    if operator == '+':
        print("{a} {operator} {b} = {add(a, b)}")
    elif operator == '-':
        print("{a} {operator} {b} = {sub(a, b)}")
    elif operator == '*':
        print("{a} {operator} {b} = {mul(a, b)}")
    elif operator == '/':
        print("{a} {operator} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)