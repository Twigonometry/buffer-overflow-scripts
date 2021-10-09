#!/usr/bin/python3

#https://github.com/gh0x0st
#gh0x0st@protonmail.com

import sys,socket 
address = sys.argv[1]
port = int(sys.argv[2])
try:
	prefix = sys.argv[3]
except:
	prefix = None

buffer = ['\x41']
counter = 100
while len(buffer)<= 10:
	buffer.append('\x41'*counter)
	counter=counter+100
try:
	for string in buffer:
		if prefix is not None:
			print('[+] Sending prefix: {}'.format(prefix))
			string = prefix + string
			prefix = None
		print('[+] Sending {} bytes...'.format(len(string)))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect=s.connect((address,port))
		s.recv(1024)
		s.send(string + '\r\n')
		print('[+] Done')
except:
 	print('[!] Unable to connect to the application. You may have crashed it.')
 	sys.exit(0)
finally:
	s.close()
