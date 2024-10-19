import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sys

#Usage Format
if len(sys.argv) != 4:
	print("Usage: python3 client.py <server IP> <port number> <key>")
	sys.exit(1)
	
#collect the arguments
SERVER_IP = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
key = sys.argv[3].encode()

# Ensure the key is 16bytes
if len(key) != 16:
	print("Error: Key must be 16 bytes long")
	sys.exit(1)
	
#Create client socket
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Attempt connection to server
cliSock.connect((SERVER_IP, SERVER_PORT))

#send the message to server 
msg = input("Plaese enter a message to send to server: ")

#Encrypt the message 
cipher = AES.new(key, AES.MODE_ECB)
padded_msg = pad(msg.encode(), 16)
encrypted_msg = cipher.encrypt(padded_msg)

#send the encrypted message to server
cliSock.send(encrypted_msg)

#close the connection
cliSock.close()
