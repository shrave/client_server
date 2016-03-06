import socket

c=socket.socket()

host ='127.0.0.1'
port=9999

c.connect((host,port))
name=raw_input('Enter username:')
c.send(name)
flag=1
while flag:
	data=raw_input('Username:Message')
	c.send(data)
	reply=c.recv(1024)
	if reply:
		print reply
	if data=='quit':
		flag=0
c.close()
#Make a mechanism if reply not there for another connection.
