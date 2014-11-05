__author__ = 'root'
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
else:
    print 'not in this block'

print 'Done'