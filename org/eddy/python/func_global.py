__author__ = 'root'
def func():
    global x
    x = 20
    print 'x is', x

x = 50
func()
print 'global x , ', x