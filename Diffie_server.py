import socket
import random as r
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
s.bind(('', port))
count=1
s.listen(5)
while True:
	c, addr = s.accept()
	print("******************************************************")
	print('Got Connection From Client No.',count,"Address=", addr)
	while True:
		temp = c.recv(1024).decode()
		prime,gen=temp.split(",")
		prime=int(prime)
		gen=int(gen)
		print("The Prime No Is="+str(prime)+"\nThe Generator Is="+str(gen))

		x = str(r.randrange(0, prime))
		print("X=" + x)
		x=int(x)
		R1=(gen**x)%prime
		print("R1="+str(R1))
		R1=str(R1).encode()
		c.send(R1)

		R2=c.recv(1024).decode()
		print("R2="+R2)
		R2=int(R2)

		key_server=(R2**x)%prime
		print("Private key For Server Is="+str(key_server))

		break
	count+=1
	c.close()
