print(f'{__file__=} {__package__=}')

from .helpers import print_func_name


def accelerating():
    print_func_name()


def breaking():
    print_func_name()