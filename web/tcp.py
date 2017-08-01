# tcp client.py
# -*- coding: utf-8 -*-

import socket

if __name__ == '__main__':
	recbuffer = []
	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s1.connect(('www.baidu.com', 80))
	s1.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
	while True:
		d = s1.recv(1024)
		if d:
			recbuffer.append(d)
		else:
			break
	s1.close()
	data = ''.join(recbuffer)

	header, html = data.split('\r\n\r\n', 1)
	print header
	# 把接收的数据写入文件:
	with open('baidu.html', 'wb') as f:
		f.write(html)
	print header