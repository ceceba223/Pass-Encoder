import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from getpass import getpass


def encrypt_data(data):
	pubKey = RSA.import_key(open("./secret/pub_key.pem").read())	#getting rsa public key
	data = data.encode('utf-8')										#convert data to bytes
	encryptor = PKCS1_OAEP.new(pubKey)								#pass public key to encryptor
	encrypted = encryptor.encrypt(data)								#encrypt data
	return(encrypted)												#returning encrypted data

def decrypt_data(data):
	master = getpass("Master password: ")

	with open('./secret/rsa_key.pem', 'r') as key_file:				#opening privat key file
		try:
			privat_key = RSA.import_key(key_file.read(), master)	#try to decode privat key with the entered master pw
		except ValueError:											#in case of wrong master pw
			print("Wrong master password\n\n")
			return
	
	decryptor = PKCS1_OAEP.new(privat_key)							#pass privat key to decryptor
	decrypted = decryptor.decrypt(data)								#decrypt data
	decrypted = str(decrypted).replace("b'", "").replace("'", "")	#clean up the data
	return(decrypted)