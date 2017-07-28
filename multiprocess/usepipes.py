# hello.py
# -*- coding: utf-8 -*-
from multiprocessing import Pipe, Process
import os

#pipe allow one writer adn one reader
#in this case, parent writer(send), child recv(get)
#so parent close out_pipe, child close in_pipe
def child_handler(pipe):
	print 'child %d start handle ' %os.getpid()
	out_pipe, in_pipe = pipe
	in_pipe.close()

	while True:
		try:
			msg = out_pipe.recv()
			print msg
		except EOFError:
			print 'child pro get eof'
			break


if __name__ == '__main__':
	out_pipe, in_pipe = Pipe()
	child_pro = Process(target=child_handler, args=((out_pipe, in_pipe),))
	child_pro.start()

	out_pipe.close()
	for x in range(101):
		in_pipe.send(x)

	in_pipe.close()
	child_pro.join()
