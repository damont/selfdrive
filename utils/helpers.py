import inspect


def print_func_name():
    func_name = inspect.stack()[1][3]
    func_pieces = ' '.join(func_name.split('_'))        
    func_pieces.capitalize()
    print(func_pieces)