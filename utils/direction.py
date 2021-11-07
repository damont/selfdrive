from .helpers import print_func_name
from .speed import breaking, accelerating

def turning_left():
    breaking()
    print_func_name()
    accelerating()
    
    
def turning_right():
    breaking()
    print_func_name()
    accelerating()
    
    
if __name__ == '__main__':
    turning_left()
    turning_right()
    