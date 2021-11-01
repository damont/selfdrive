import inspect


def print_func_name():
    func_name = inspect.stack()[1][3]
    func_pieces = ' '.join(func_name.split('_'))        
    func_pieces.capitalize()
    print(func_pieces)
        

def accelerating():
    print_func_name()


def breaking():
    print_func_name()


def turning_left():
    breaking()
    print_func_name()
    accelerating()
    
    
def turning_right():
    breaking()
    print_func_name()
    accelerating()
    

def driving():
    print_func_name()
    
    
if __name__ == '__main__':
    driving()