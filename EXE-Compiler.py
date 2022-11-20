# initial imports #
import sys
import os
# initial imports end #

os.system("clear")


## Base Python Import Check ##
try:
	import pylibcheck
except ImportError as error:
	print(error, 'Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install pylibcheck')
		import pylibcheck
		os.system("clear")
		print('pylibcheck is now installed')
	elif choice == 'N':
		print('Suit yourself then.')
		sys.exit()
	else:
		print('invalid choice')
		sys.exit()

## Use pylibcheck to check for / install pyinstaller
if not pylibcheck.checkPackage("pyinstaller"):
	os.system("clear")
	print('pyinstaller doesn\'t exist. Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install pyinstaller')
		os.system("clear")
		print('pyinstaller is now installed')
	elif choice == 'N':
		print('Suit yourself then.')
		sys.exit()
	else:
		print('invalid choice')
		sys.exit()
else:
	print("pyinstaller is installed? : True")

scriptPath = input('\nPath to Python Script: ')

def CompileScript():
	os.system("clear")
	print("Compiling Python Script to Executable File\n\n")
	os.system(f"pyinstaller --onefile {scriptPath}")
	print('\n\nCompilation Complete')
	sys.exit()

CompileScript()