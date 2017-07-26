# make list
# -*- coding: utf-8 -*-

l1 = [x*x for x in range(1, 11)]
print l1

l2 = [x*x for x in range(1, 11) if x & 1 == 0]
print l2

l3 = [s1+s2 for s1 in 'ABC' for s2 in 'XYZ']
print l3

import os
l4 = [d for d in os.listdir('.')]
print l4

#generator
g = (x*x for x in range(11))
for val in g:
	print val

#如果一个函数定义中包含yield关键字
#返回的是generator
#在每次调用next()的时候执行
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(x):
	n, a, b = 0, 0, 1
	while n < x:
		yield a
		a, b = b, a+b
		n = n+1

fibget = fib(6)
print fibget.next()
print fibget.next()
print fibget.next()
for val in fibget:
	print val