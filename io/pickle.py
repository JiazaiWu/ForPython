# hello.py
# -*- coding: utf-8 -*-

try:
	import cPickle as pickle
except ImportError:
	import pickle

d1 = {'name':'jiazai', 'score':100}

print pickle.dumps(d1)

f1 = open('dump.txt', 'wb')
pickle.dump(d1, f1)
f1.close()

f2 = open('dump.txt', 'r')
d2 = pickle.load(f2)
print d2