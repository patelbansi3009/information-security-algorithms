import socket
import random as r
import sympy as sy


def create_gen(prime):
	return (r.randrange(2,prime-2))

prime=sy.randprime(2,500000)
print("The Prime Number is="+str(prime))
gen=create_gen(prime)
print("The Generator is="+str(gen))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
s.connect(("127.0.0.1", port))


while True:
	y= str(r.randrange(0, prime))

	prime=str(prime)+","
	prime=prime.encode()
	s.send(prime)
	gen=str(gen).encode()
	s.send(gen)

	R1= s.recv(1024).decode()
	print("Y=" + y)
	print("R1="+R1)
	R1=int(R1)

	y=int(y)
	gen=int(gen.decode())
	prime = int(prime.decode().replace(",",""))
	R2 = (gen ** y) % prime
	print("R2=" + str(R2))
	R2 = str(R2).encode()
	s.send(R2)

	key_client=(R1**y)%prime
	print("Private key For Client Is="+str(key_client))

	break;
s.close()