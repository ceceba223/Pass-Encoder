from rule import format_txt
from rule import encode

from passwd_gen import generate

from save_load import save
from save_load import load

from key_setup import rsa_init
from colorama import Fore, init, deinit


def banner(): #print banner and Welcome text
	print("""

 ██████╗░░█████╗░░██████╗░██████╗  ███████╗███╗░░██╗░█████╗░░█████╗░██████╗░███████╗██████╗░
 ██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ██████╔╝███████║╚█████╗░╚█████╗░  █████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝
 ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗  ██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗
 ██║░░░░░██║░░██║██████╔╝██████╔╝  ███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║
 ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")
	print("Weclome to PASS ENCODER an open-source password generator and encoder!\n\n")

def menue():	#show menue
	print("Choose an action from the menue below:")
	print("""
[\033[36m1\033[0m] Create password by rule
[\033[36m2\033[0m] Generate random password
[\033[36m3\033[0m] Access a saved password
[\033[36m4\033[0m] Store password
[\033[36m5\033[0m] Exit
""")
	select = input("Option: ")
	load_option(select)

def load_option(select):	#load selected functions
	try:
		select = int(select)
	except ValueError:
		print("\033[31mNot a valide nummber, try again!\033[0m")
		menue()

	if select == 1:
		rule()
	elif select == 2:
		passwd_gen()
	elif select == 3:
		load_passwd()
	elif select == 4:
		save_passwd()
	else:
		print("\n\033[0mexiting ...")
		print("Bye!")
		deinit()	#colorama deinit
		exit()


def rule():		#Create passwd by rule
	print("\n\033[1mCreate password by rule:\033[0m")
	print("Input clear text password:")
	text = input()

	text = format_txt(text)
	encoded = encode(text)
	print(f"\n\033[36m{encoded}\033[0m\n\n")
	menue()

def passwd_gen():	#genarete random passwd
	print("\n\033[1mGenerate a random Password:\033[0m")
	passwd = generate()
	print(f"\033[36m{passwd}\033[0m")

	temp = input("Do you want to save this password? [Y/N] ").lower()
	if temp == "y":
		name = input("Under what name should this password be saved: ")
		save(passwd, name)
	else:
		print("\n\n")
	menue()

def load_passwd():
	print("\n\033[1mLoad password:\033[0m")
	name = input("Password name: ")
	load(name)
	menue()

def save_passwd():	#save passwd
	print("\n\033[1mSave password:\033[0m")

	passwd = input("Password: ")
	name = input("Password name: ")
	save(passwd, name)
	menue()

def main():
	rsa_init()
	init()	#colorama init()
	banner()
	menue()

if __name__ == '__main__':
	main()