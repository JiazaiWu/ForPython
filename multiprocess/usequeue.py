# hello.py
# -*- coding: utf-8 -*-

from multiprocessing import Queue, Process, Pool, Manager
from Queue import Empty as QueueEmpty
import os
import random

#queue use put and get/put 
def getter(name, queue):
    print 'Son process %s' % name
    while True:
        try:
            value = queue.get(True, 2)
            # block为True,就是如果队列中无数据了。
            #   |—————— 若timeout默认是None，那么会一直等待下去。
            #   |—————— 若timeout设置了时间，那么会等待timeout秒后才会抛出Queue.Empty异常
            # block 为False，如果队列中无数据，就抛出Queue.Empty异常
            print "Process %d getter get: %d" % (os.getpid(), value)
        except QueueEmpty:
            break


def putter(name, queue):
    print "Son process %s" % name
    for i in range(0, 1000):
        #value = random.random()
        value = i
        queue.put(value)
        # 放入数据 put(obj[, block[, timeout]])
        # 若block为True，如队列是满的：
        #  |—————— 若timeout是默认None，那么就会一直等下去
        #  |—————— 若timeout设置了等待时间，那么会等待timeout秒后，如果还是满的，那么就抛出Queue.Full.
        # 若block是False，如果队列满了，直接抛出Queue.Full
        print "Process %d putter Put: %d" % (os.getpid(), value)

if __name__ == '__main__':
	#进程池中使用队列则要使用multiprocess的Manager类
    manager = Manager()
    # 父进程创建Queue，并传给各个子进程：
    queue = manager.Queue()
    p = Pool()
    p.apply_async(getter, args=("Getter", queue))
    p.apply_async(putter, args=("Putter", queue))
    p.close()
    p.join()