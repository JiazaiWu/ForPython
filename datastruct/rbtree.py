# rbtree.py
# -*- coding: utf-8 -*-
#default compare function
def default_compare(leftval, rightval):
	if leftval < rightval:
		return (True. leftval)
	elif leftval > rightval:
		return (False, rightval)
	else:
		return (False, None)

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

		def show_value(self):
			print 'color %s value %d' %('red' if self.color == 0 else 'black', self.value)

	def __init__(self, value=None):
		if value != None:
			self.root = self.rbtree_node(value)
			self.root.parent = self.root
			self.root.color = 1
		self.compare_function = default_compare


	def inter_node(self, node):
		if self.root == None:
			self.root = node
			self.root.color = 1
			return

		pnode = self.root
		while True:
			ret, val = self.compare_function(pnode.value, node.value)
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
	nnode = rbtree.rbtree_node(5)
	mtree.inter_node(nnode)