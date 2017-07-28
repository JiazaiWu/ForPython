# hello.py
# -*- coding: utf-8 -*-
import codecs
import os
#import shutil <-- this module enhanced os, such as copy function

with open('text', 'r') as f1:
	print f1.readline().strip()#use strip to erase certain char, default \n &' '

with open('text', 'r') as f2:
	for line in f2.readlines():
		print line.strip()

#with codecs.open('zh', 'r', 'gbk') as f3:
#	f3.read()

with open('test', 'w') as f4:
	f4.write('Hello World!\n')

with open('zh-test', 'w') as f5:
	f5.write('中文\n')

#print dir(os)
print os.name
print os.uname()
#print os.environ <--TOO MANY
print os.getenv('PATH')

#how to new a dir
this_path = os.path.abspath('.')
print this_path
new_path = os.path.join(this_path, 'newdir')
print new_path
print os.path.isdir(new_path)
#os.mkdir(new_path) <-- need to check if dir exist
split_path = os.path.split(new_path)
print split_path

print [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']