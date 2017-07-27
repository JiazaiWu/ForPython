# hello.py
# -*- coding: utf-8 -*-

import types
#stduent is extended from object
class student(object):
	def __init__(self, name, score):
		#__member can not be seen out of class
		self.__name = name
		self.score = score

	def print_stu_score(self):
		print '%s get %s' %(self.__name, self.score)

bart = student('jiazai', 90)
bart.print_stu_score()
#print bart.__name <---build break
print bart.score

class Animal(object):
	def run(self):
		print 'An animal is running!'

class Cat(Animal):
	pass

class Dog(Animal):
	def run(self):
		print 'A dog is running!'

cat = Cat()
cat.run()

dog = Dog()
dog.run()

print isinstance(cat, Cat)

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(dog)

print type(123) == types.IntType
print type(dog) == Dog
#'type()' is strict type check
print type(dog) == Animal#this is false!!
#use isinstance to check extend relation ship
print isinstance(dog, Animal)#this is true!!

print hasattr(dog, 'y')
setattr(dog, 'y', 19)
print hasattr(dog, 'y')
print 'dog y attr is', dog.y

#yes!!!
print hasattr(dog, 'run')
print hasattr(dog.run, '__call__')
print callable(dog.run)