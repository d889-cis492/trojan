import os

def run( **args ):					# variable number of arguments
	print "[*] In dirlister module"
	return str(os.listdir('.'))			# part of os module, returns the current directory of where it is running
