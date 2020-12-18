#!/usr/bin/python -tt
import socket
import os
import os.path
import operator
import tqdm
import sys

#def client_program():
host = '192.168.43.219'
port = 445
client_socket = socket.socket()
client_socket.connect((host, port)) #connect to the server
while True:
	print('***********************************************************************')
	print('***********************WELCOME TO THE SERVER!!!************************')
	print('***********************************************************************')
	message = input("Do you download or send a file?( download / send / delete ): ") #take input
	client_socket.send(message.encode('utf-8'))
	filename_txt = input('Enter the name of the file: ')
	client_socket.send(filename_txt.encode('utf-8'))

	if message == 'download':
		file = open(filename_txt, "wb")
		print('File is being transfer/download...')
		client = client_socket.recv(1024)
		while(client):
			file.write(client)
			client = client_socket.recv(1024)
		file.close()
		print('Download / Received completed')
	elif message == 'send':
		file = open(filename_txt, "wb")
		print('File is being send to the server...')
		client = file.read(1024)
		while(client):
			client_socket.send(client)
			client = file.read(1024)
		file.close()
		print('Seding txt file is completed')
	elif message == 'delete':
		file = open(filename_txt, "wb")
		print('File is being deleted . .')
		client = file.read(1024)
		while(client):
			client_socket.send(client)
			client = file.read(1024)
		file.close()
		print('Delete file was successfull')

	elif message.lower().strip() != 'bye':

		client_socket.send(message.encode()) #send message
		data = client_socket.recv(1024).decode() #receive response
		print('Received from server: ' + data) #show in terminal

		message = input(" -> ") #again take input

	client_socket.close() #close the connection


#if __name__ == '__main__':
	#client_program()
