# hello.py
# -*- coding: utf-8 -*-

from types import MethodType
class student(object):
	#use __slots__ to lock attr
	__slots__ = ('name', 'score', 'show', 'height', '__name', '__score', '__height')
	#__str__ is for print this class
	def __str__(self):
		return 'student str is '+self.name
	__repr__ = __str__
	def __init__(self, name, score):
		#__member can not be seen out of class
		self.name = name
		self.score = score

	#height can use as attr
	@property
	def height(self):
		return self.__height

	#followed after @property
	@height.setter
	def height(self, value):
		print 'set height for', self.name
		self.__height = value

s1 = student('wu', 99)
#setattr(s1, 'age', 19) <-- this will BB for 'age' is not in the slots

def add_score(self):
	print self.name, "score added"
def show_name(self):
	print 'My name is', self.name
student.new_func = MethodType(add_score, None, student)

s2 = student('jiazai', 100)

s1.new_func()
s2.new_func()


s2.show = MethodType(show_name, s2, student)
s2.show()
#s1.show() <-- bb, no show attr in s1

class super_stu(student):
	pass

ss = super_stu('zai', 60)
ss.age = 23 # it is OK, __slots__ only for the marked class, will not be extended to child class
print ss.age
print ss.name

s1.height = 176
print s1