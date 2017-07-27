# hello.py
# -*- coding: utf-8 -*-
import time
import functools

#@log
#def now equals to
#now = log(now)
def log(func):
	@functools.wraps(func)#if no this, print now.__name__  will be wrapper
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper#notice this is return define

@log
def now():
	print time.strftime('%Y-%m-%d',time.localtime(time.time()))

print now.__name__



#execise 1
def mlog(func):
	@functools.wraps(func)#if no this, print now.__name__  will be wrapper
	def wrapper(*args, **kw):
		print 'begin call %s():' % func.__name__
		ret = func(*args, **kw)
		print 'end call %s():' % func.__name__
		return ret
	return wrapper

@mlog
def f1():
	print 'f1 do something..'
f1()


#execise 2
def nlog(arg):

    def actual_log(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s call %s()' % (arg, func.__name__)
            return func(*args, **kw)
        return wrapper

    #input arg is function name now
    def highwrapper(*args, **kw):
        print '%s() called' % arg.__name__
        return arg(*args, **kw)

    if not isinstance(arg, str):
        return highwrapper
    else:
        return actual_log

@nlog('jiazai')
def f2():
	print 'f2 do something'

@nlog
def f3():
	print 'f3 do something'

f2()
f3()
