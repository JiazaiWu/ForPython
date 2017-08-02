# matrix.py
# -*- coding: utf-8 -*-

from numpy import *

if __name__ == '__main__':
	l1 = [[1,2], [0, 3]]
	a1 = mat(l1)
	print a1

	a2 = mat(zeros((3, 3)))
	print a2

	a3 = mat(ones((2,2)))
	print a3

	#这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，需要将其转换成#matrix
	a4=mat(random.randint(10,size=(3,3)));
	print a4

	a5 = a3*a3
	print a5

	print a1.T
	print a1.I
	print a1.I * a1

	#calculate matrix det
	print linalg.det(a3)