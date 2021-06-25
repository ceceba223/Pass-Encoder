import random
import string


def generate():		#generate and return a random 24 character string
	characters = string.ascii_letters + string.digits + string.punctuation
	passwd = ''.join(random.choice(characters) for i in range(24))
	return(passwd)