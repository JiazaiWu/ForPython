# hello.py
# -*- coding: utf-8 -*-
#Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

import time, threading

def thr_func():
	print 'Thread %s is running...' %threading.current_thread().name
	n = 0
	while n < 5:
		n = n + 1
		print 'thread %s >>> %s' % (threading.current_thread().name, n)
		time.sleep(1)
	print 'thread %s ended.' % threading.current_thread().name

#balance shoule be 0
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        global lock
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

if __name__ == '__main__':
	#t = threading.Thread(target=thr_func, name='jiazai_thread')
	#t.start()
	#t.join()
	#print 'thread %s ended.' % threading.current_thread().name

	t1 = threading.Thread(target=run_thread, args=(5,))
	t2 = threading.Thread(target=run_thread, args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print balance