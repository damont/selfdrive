import sys
print(sys.path)
if '__package__' in dir() and __package__:
    print(__package__)
    from .speed import slow_down, speed_up
else:
    from speed import slow_down, speed_up

def turn_left():
    slow_down()
    print('Im turning left')
    speed_up()
    
    
def turn_right():
    slow_down()
    slow_down()
    print('Im turning right')
    speed_up()
    
    
if __name__ == '__main__':
    turn_left()
    turn_right()