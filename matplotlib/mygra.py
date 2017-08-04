# rbtree.py
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

if __name__ == '__main__':
	print 7/2
	c = 'r' if 0 == 0 else 'k'
	x_axis = range(1, 31)
	y_axis = range(1, 31)
	#plt.plot(x_axis, y_axis) 这个是画线
	#第一个参数是y轴的位置，第二个参数是具体标签
	#plt.figure(1)
	plt.xticks(x_axis, x_axis, rotation=0)
	plt.yticks(y_axis, y_axis, rotation=0)
	#plt.grid()

	plt.annotate('local max', xy=(3, 1.5), xytext=(3, 1.5), color='k')
	plt.annotate('local max', xy=(6, 6.5), xytext=(5, 4.5),
            arrowprops=dict(arrowstyle="-", ),color=c
            )
	plt.show() 
	#
	#plt.figure(2)
	#plt.show()