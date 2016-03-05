import socket
import thread
import threading
import sys

port = 9999
class Server(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.host='127.0.0.1'
		self.port= 9999
		self.size= 1024
		self.server=socket.socket()
		self.users= []
	
		try:
			#self.server=socket.socket()
			self.server.bind((self.host,self.port))
			self.server.listen(5)
		except socket.error as err:
			print "Connection closed due to %s" %(err)
			self.server.close()
		#Check code here.
	def run(self):
		print 'Waiting for connections'
		while True:
			c, addr = self.server.accept()
			threading.Thread(target=self.thread_run(),args=(c, addr)).start()

	def thread_run(self,c,addr):
		print 'Client connected with' + addr 
		while True:
			data =c.recv(self.size)
			print data
			reply=raw_input('->')
			c.send(reply)
			if data=='quit':
				c.close()
				break
	 
		
S=Server()










