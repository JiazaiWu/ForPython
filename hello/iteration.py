# iterate in dictionary.py
# -*- coding: utf-8 -*-

d = {'a':1, 'b':2, 'c':3}

for key in d:
	print key

for val in d.itervalues():
	print val

for key, val in d.iteritems():
	print key, val

from collections import Iterable
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

for i, val in enumerate(['A', 'B', 'C']):
	print i, val