"""
Entry point for our self driving system
"""
from utils.helpers import print_func_name
from utils.speed import accelerating


def driving():
    print_func_name()
    accelerating()
    
    
if __name__ == '__main__':
    driving()