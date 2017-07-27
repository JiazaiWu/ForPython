# hello.py
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print 'An animal is running!'

class Cat(Animal):
    def run(self):
        print 'A cat is running!'

class Dog(Animal):
    def run(self):
        print 'A dog is running!'

class Mix1(Dog, Cat):
    pass

class Mix2(Cat, Dog):
    pass

mix1 = Mix1()
mix1.run() #<-- dog run

mix2 = Mix2();
mix2.run() #<-- cat run