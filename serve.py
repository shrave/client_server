import socket
import sys
import threading
sockdict={}
thread_send=[]
thread_rcv=[]
sckt = socket.socket()
sckt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_address = ('127.0.0.1', 9999)
sckt.bind((server_address))
sckt.listen(5) 

print "Server is ready"

c1 , addr1=sckt.accept()
username1=c1.recv(1024)
if username1:
        sockdict[username1]=c1
        print username1+ " connected"
        c1.send(username1+ " connected")

c2, addr2=sckt.accept()
username2=c2.recv(1024)
if username2:
        print username2+ " connected"
        c2.send(username1+ " connected")
        sockdict[username2]=c2

c3, addr3=sckt.accept()
username3=c3.recv(1024)
if username3:
        print username3+ " connected"
        c3.send(username1+ " connected")
        sockdict[username3]=c3
c1=socket.socket()
flag=1
while flag:
        data1=c1.recv(1024)
        data2=c2.recv(1024)
        data3=c3.recv(1024)
        if data1 or data2 or data3:
                if data1:
                        thread_rcv.append(threading.Thread((client_recv()),(c1,data1)).start())
                        #thread_send[-1].start()
                if data2:
                        thread_rcv.append(threading.Thread((client_recv()),(c2,data2)).start())
                        #thread_send[-1].start()
                if data3:
                        thread_rcv.append(threading.Thread((client_recv()),(c3,data3)).start())
                        #thread_send[-1].start()
                else:
                        flag=0

#sockdict={}
def client_send(socket,message):
	socket.send(message)

def client_recv(socket,reply):
	username=reply.split(':')[0]
	sock=sockdict[username]
	message=reply.split(':')[1]
	thread_send.append(threading.Thread((client_send()),(sock,message)).start())

#First three clients will be connected.
#Create receiving threads and analyse that data.
#Complete if statements put in while loop.
