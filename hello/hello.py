# hello.py
# -*- coding: utf-8 -*-

name = raw_input('please input your name: ')
print 'hello, world', name
a = 100
if a >= 50:
	print a
else:
	print -a

#string operate: replace()
str1 = 'abc'
str2 = str1.replace('a', 'A')
print str1
print str2

# \\\t\\\ showed
print r'\\\t\\'

#hello
#jiazai
#bye     showed
print '''hello
jiazai
bye'''

x = ord('A')
print x

#[] for list
testlist = ['c', 'b', 'a']
testlist.sort()
print testlist
classmates = ['YE', 'JIAZAI', 'MEIMEI', ['you', 'me']]
print len(classmates)
print classmates
print[s.lower() for s in classmates if isinstance(s, str)]


sum = 0
for x in range(101):
	sum = sum + x
print sum

#() for tuple, ignore

#{} for dictionary - map
di = {'jiazai':176, 'bob':177}
print di['jiazai']

da = {}
da['jiazai'] = 6
print da['jiazai']


# = set() for set
#add() remove() to add/remove member
#also support | and & operate
mset = set([1, 2, 3, 3])
print mset
mset.add(4)
mset.remove(3)
print mset

s2 = set([7, 8, 9])

s3 = s2 | mset
print s3