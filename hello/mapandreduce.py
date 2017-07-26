# map and reduce
# -*- coding: utf-8 -*-

def f(x):
	return x*x

def add(x, y):
	return x+y

print map(f, [1,2,3,4,5])

# =f(f(f(f(x1, x2), x3), x4), x5)
print reduce(add, [1,2,3,4,5])

#execise 1
def checkname(name):
	return name.capitalize()


print map(checkname, ['adam', 'LISA', 'barT'])

#execise 2
def mul(x, y):
	return x*y

print reduce(mul, [1,2,3,4,5,6])

#execise 3
def not_prime(val):
	n = 2
	while n < val/2:
		if not val%n:#除尽 == 没有余数 == 素数
			return True
		n = n+1
	return False


print filter(not_prime, range(1, 101))

def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
             return j*j
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1()#1
print f2()#4
print f3()#9