# hello.py
# -*- coding: utf-8 -*-

#use isinstance() to check type
def func(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad arge type')
	print x
	if x >= 0:
		return x, x
	else:
		return -x, -x

#variable arge, use *
def funcvariable(*x):
	sum = 0;
	for val in x:
		sum = sum + val
	print sum

#test func blow
v1, v2 = func(3.14)
print v1, ' ', v2

funcvariable(1, 2, 3)
t1 = (1, 2, 3)
funcvariable(*t1)