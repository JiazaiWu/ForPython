# hello.py
# -*- coding: utf-8 -*-

#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
#loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
import json

d = {'name':'jiazai', 'score':100, 'age':24}
print json.dumps(d)

f1 = open('mjson', 'wb')
json.dump(d, f1)
f1.close()

#all str from json load will be unicode format
f2 = open('mjson', 'r')
d2 = json.load(f2)
print d2


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def  dic2Student(dic):
	return Student(dic['name'], dic['age'], dic['score'])

#dumps and load
s1 = Student('jiazai', 24, 100)
dumped_s1 = json.dumps(s1.__dict__)
print dumped_s1
s2 = json.loads(dumped_s1, object_hook=dic2Student)
print s2.name
print s2.age
print s2.score