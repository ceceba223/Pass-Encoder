import json
from Crypto.PublicKey import RSA
from encryption import encrypt_data
from encryption import decrypt_data

def save(passwd, name):													#save pw to ./secret/passwords/
	passwd = encrypt_data(passwd)										#encrypt passwd
	with open('./secret/passwords/' + name + '.txt', 'wb') as file:		#create file for password
		file.write(passwd)												#save password to file
		file.close()													#close file
	print(f"\nYour password has been saved as \033[36m{name}\033[0m\n\n")

def load(name):															#load pw from file
	try: file = open('./secret/passwords/' + name + '.txt', 'rb')		#try to open file
	except FileNotFoundError:											#in case password file does not exist
		print("This password does not exist\n\n")
		return()
	passwd = file.read()												#read password hash from file
	passwd = decrypt_data(passwd)										#decrypt the password
	if passwd == None:													#incase the master password is wrong
		return()
	print(f"\033[36m{passwd}\033[0m\n\n")														#print the password