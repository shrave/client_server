import socket

port=9999
host='127.0.0.1'

clist=[]

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(10)

c, addr=s.accept()
#clist.append(addr)


'''
#while clist:
	c, addr=s.accept()
	clist.append(addr)
	#Initially the user gives the chatpartner ip
	chatp=c.recv(1024)
	for tup in clist:
		if tup[0]==chatp:
'''			
while True:
       		 #c, addr=s.accept()
	data = c.recv(1024)
        print data
        reply=raw_input('->')
        c.send(reply)
        if data=='quit':
			#clist.remove(addr)
		c.close()
                break


'''
while True:
	#c, addr=s.accept()
	data = c.recv(1024)
	print data
	reply=raw_input('->')
	c.send(reply)
	if data=='quit':
		c.close()
		break'''
	'''if data == 'quit':
		c.close()		
		break'''

	

