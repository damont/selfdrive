import sys
print(f'{__file__=} {sys.path[0]=}')

from helpers import print_func_name


def accelerating():
    print_func_name()


def breaking():
    print_func_name()