__author__ = 'root'
def func(x):
    print 'X is ', x
    x = 2
    print 'Changed local x to ', x

x = 50
print 'x is still ', x
func(20)