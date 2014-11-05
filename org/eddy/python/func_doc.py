__author__ = 'root'

def printMax(x, y):
    '''Prints the maximum of two numbers.
     The two values must be integers.'''
    x = int(x) # convert to integer
    y = int(y)
    if x > y:
        print x, 'is max'
    else:
        print y, 'is max'

printMax(3, 5)
print printMax.__doc__
help(printMax)