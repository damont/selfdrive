from driveutils.turning import turn_right


def drive():
    print('Im driving')
    uturn()
    
    
def uturn():
    turn_right()
    turn_right()
    
    
if __name__ == '__main__':
    drive()