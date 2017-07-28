# hello.py
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process#window sys use this 

#child process will not print this
print 'process %d started!!' %os.getpid()

pid = os.fork()
if pid == 0:
	print 'child process %d, parent is %d' %(os.getpid(), os.getppid())
else:
	print 'process %d just created a child' %os.getpid()

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()#<--wait here utill p handled
    print 'Process end.'