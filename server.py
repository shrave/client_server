import socket

port=9999
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(),port))
serversocket.listen(5)
while 1:
	clients,addr = serversocket.accept()
	clients.send('Connection established')
	clients.close()

