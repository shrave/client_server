import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=9999

#ping all ips and connect to a specific ip.Save that ip as sip
'''ip=[0,0,0,1]
for i in range(256):
	k='.'.join(ip)
	if s.connect((k,port)):
		s.connect((k,port))
		sip=k
		break
	ip=map(lambda x:x+1,ip)
	if ip[0]==255:
		break
'''
for i in range(256):
	for j in range(256):
		for k in range(256):
			for l in range(256):
				if s.connect((i.j.k.l,port)):
					s.connect((i.j.k.l,port))
					sip='i.j.k.l'
					break
#192.168 is fixed.

print s.recv(1024)
s.close



