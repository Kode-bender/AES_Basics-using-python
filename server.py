import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys

#Usage Format
if len(sys.argv) != 3:
	print("Usage: python3 server.py <port number> <key>")
	sys.exit(1)
	
#collect the arguments
PORT_NUMBER = int(sys.argv[1])
key = sys.argv[2].encode()

# Ensure the key is 16bytes
if len(key) != 16:
	print("Error: Key must be 16 bytes long")
	sys.exit(1)
	
#Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associate the socket with the port
serverSock.bind(('', PORT_NUMBER))

#Start listening  for incoming connections
serverSock.listen(100)

#Keep accepting connection forever
while True:
	print("Waiting for client to connect...")
	
	#Accep a waiting connection
	cliSock, cliInfo = serverSock.accept()
	print("Client connected from:" + str(cliInfo))
	
	#Receive encrypted message from the client
	encrypted_msg = cliSock.recv(1024)
	
	#Decrypt the message
	cipher = AES.new(key, AES.MODE_ECB)
	decrypted_msg = unpad(cipher.decrypt(encrypted_msg), 16)
	
	#print decrypted message
	print("Decrypted message from client:" + decrypted_msg.decode())
	
	#Hang up client connection
	cliSock.close()
