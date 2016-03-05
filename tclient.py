import socket
import sys
import threading

class Client(object):
	def __init__(self,port,host):
		self.host=host
		self.port=port
		self.client=socket.socket()
		#self.client.connect((self.host,self.port))

	def communicate(self):
		while True:
			message=raw_input('->')
			self.client.send(message)
			reply=self.client.recv(1024)
			print reply
			if message=='quit':
				self.client.close()
				break

c=Client(9999,'127.0.0.1')
Client.client.connect((Client.host,Client.port))
Client.communicate()			
