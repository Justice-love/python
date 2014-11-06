__author__ = 'root'

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = file('poem', 'w')
f.write(poem)
f.close()

f = file('poem')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print  line,

f.close()