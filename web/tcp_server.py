# tcp server.py
# -*- coding: utf-8 -*-

import socket
import threading
import time

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

if __name__ == '__main__':
	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s1.bind(('127.0.0.1', 10000))
	s1.listen(10)
	print 'server is listening...'

	while True:
		#recevice a new connection
		print 'wait a connection'
		sock, addr = s1.accept()
		print 'get a connection'

		#new a thread to handle
		t = threading.Thread(target=tcplink, args=(sock, addr))
		t.start()

	s1.close()