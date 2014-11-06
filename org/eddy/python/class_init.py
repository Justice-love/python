__author__ = 'root'


class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print 'Hello, my name is', self.name


p = Person('Eddy')

p.sayHi()