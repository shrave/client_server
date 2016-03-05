#!/usr/bin/env python

import socket, threading

ipdict={}
clist=[]

class ClientThread(threading.Thread):

    def __init__(self,ip,port,socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
	self.socket=socket
        print "[+] New thread started for "+ip+":"+str(port)
	username=self.socket.recv(1024)
	self.username=username
	ipdict[username]=(self.socket)
	clist.append((self.username,self.port))	

    def run(self):    
        print "Connection from : "+ip+":"+str(port)

        self.socket.send("\nWelcome to the server\n\n")
	#After this stage, if you receive a message, then, dont do the steps below.
	
#dEMARK THIS STAGE or maek a new function.
	conn=self.socket.recv(1024)
	if conn in ipdict.keys():
		otherclient=ipdict[conn]
		self.socket.send(conn+" is connected!") 
	else:
		self.socket.send("The user is not online.")
#Want to make a connection feature.
		#Add an extra chance to type the username.
        #Make a yes/no question.

        while len(data):
            data = self.socket.recv(1024)
            print conn+" sent : "+data
            otherclient.send("You sent : "+data)
	#Check other clients side too.If this runs.


        print "Client disconnected..."
	#socket closing.

host = "127.0.0.1"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print "\nListening for incoming connections..."
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port,clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()


