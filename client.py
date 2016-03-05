import socket

c=socket.socket()

host ='127.0.0.1'
port=9999

c.connect((host,port))
print c.recv(1024)
name=raw_input('Enter username:')
c.send(name)
#Sending username first.
#Store the username in a dict with its socket.
user=raw_input("Please enter the username you want to talk to:")
#Exclusive connection to this username.
#Add if condition to the connetion to see if the user is online in server. 
c.send(user)
print c.recv(1024)
#c.send("quit")
while data:
	data=raw_input("->")
	c.send(data)
        if data=='quit':
		c.close()
	reply=c.recv(1024)
	print reply
	'''if data=='quit':
		c.close()'''

#Make a mechanism if reply not there for another connection.
