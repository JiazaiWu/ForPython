# rbtree.py
# -*- coding: utf-8 -*-
#default compare function
import matplotlib.pyplot as plt

def default_compare(leftval, rightval):
	if leftval < rightval:
		return (True, leftval)
	elif leftval > rightval:
		return (False, rightval)
	else:
		return (False, None)

def draw_node(node, x, y, h, px=None, py=None):
	c = 'r' if node.color == 0 else 'k'
	strval = str(node.value)
	if px == None and py == None:
		#there xy can not = None
		plt.annotate(strval, xy=(0, 0), xytext=(x, y), color=c)
	else:
		plt.annotate(strval, xy=(px, py), xytext=(x, y), arrowprops=dict(arrowstyle="-", ), color=c)
	if node.leftchild != None:
		draw_node(node.leftchild, x-16.0/h, y-h, 2*h, x, y)
	if node.rightchild != None:
		draw_node(node.rightchild, x+16.0/h, y-h, 2*h, x, y)

class rbtree(object):
	class rbtree_node(object):
		def __init__(self, value):
			self.value = value
			self.color = 0
			self.leftchild = None
			self.rightchild = None
			self.parent = None

		def set_as_left(self, node):
			self.leftchild = node
			node.parent = self

		def set_as_right(self, node):
			self.rightchild = node
			node.parent = self

		def node_height(self):
			pnode = self
			#Nil leaf considered as black node, so h default is 1
			h = 1
			while pnode != None:
			 	if pnode.color != 0:
			 		h = h + 1
			 	pnode = pnode.leftchild
			return h



		def show_all(self):
			x_axis = range(1, 31)
			y_axis = range(1, 31)
			plt.xticks(x_axis, x_axis, rotation=0)
			plt.yticks(y_axis, y_axis, rotation=0)
			x = 15
			y = 29.5
			h = 2 
			draw_node(self, x, y, h)
			plt.show()

	def __init__(self, value=None):
		if value != None:
			self.root = self.rbtree_node(value)
			self.root.parent = self.root
			self.root.color = 1
		self.compare_function = default_compare

	def set_compare_func(self, func):
		self.compare_function = func

	#gei height of tree
	def get_height(self):
		if self.root != None:
			return self.root.node_height()
		return 0

	def show_tree(self):
		if self.root != None:
			self.root.show_all()
		else:
			print 'EMPTY TREE!!!!!'

	def inter_node(self, node):
		if self.root == None:
			self.root = node
			self.root.color = 1
			return

		pnode = self.root
		while True:
			ret, val = self.compare_function(node.value, pnode.value)
			if val == None:
				return
			elif ret == True:
				if pnode.leftchild != None:
					pnode = pnode.leftchild
				else:
					pnode.set_as_left(node)
					return
			else:
				if pnode.rightchild != None:
					pnode = pnode.rightchild
				else:
					pnode.set_as_right(node)
					return


	def adjust_tree(self, node):
		pass

if __name__ == '__main__':
	mtree = rbtree(10)
	lnode = rbtree.rbtree_node(5)
	rnode = rbtree.rbtree_node(11)
	mtree.inter_node(lnode)
	mtree.inter_node(rnode)
	mtree.inter_node(rbtree.rbtree_node(6))
	mtree.inter_node(rbtree.rbtree_node(7))
	mtree.show_tree()