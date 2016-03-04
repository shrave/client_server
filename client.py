import socket

c=socket.socket()

host ='127.0.0.1'
port=9999

c.connect((host,port))

name=raw_input('Enter username:')
data=raw_input("->")
c.send(data)
print c.recv(1024)
#c.send("quit")
while data:
	data=raw_input("->")
	c.send(data)
	k=c.recv(1024)
	print k
	if k=='quit':
		c.close()


