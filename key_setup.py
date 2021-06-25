import json
from Crypto.PublicKey import RSA
from getpass import getpass


def master_setup():
	passwd1 = getpass("Enter your new master password: ")
	passwd2 = getpass("Repeat your master password: ")
	if passwd1 == passwd2:
		print("Your master password has been set")
		return(passwd1)
	else:
		print("Passwords don't match, try again!")
		master_setup()

def rsa_init():
	try:														#test if keys have already been set up
		open('./secret/rsa_key.pem', 'x')
	except FileExistsError:										#in case the configuration file exists
		return()

	key = RSA.generate(1024)									#generate RSA keys
	with open('./secret/rsa_key.pem', 'wb') as key_file: 		#create file for privat key
		master = master_setup()									#set master password
		key_file.write(key.export_key('PEM', master))			#write privat key to file
		key_file.close()										#close privat key file
	with open('./secret/pub_key.pem', 'wb') as pubKey_file:		#create file for public key	
		pubKey_file.write(key.publickey().export_key('PEM'))	#write public key to file
		pubKey_file.close()										#close public key file