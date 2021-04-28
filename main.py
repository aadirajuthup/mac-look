import sys
import json
from colors import *
from os import system
import urllib.request as urllib


url = 'https://macvendors.co/api/'

def invalid():
	sys.stdout.write(RED)
	print('\n[-] Invalid MAC Address\n')
	sys.stdout.write(RESET)
	if __name__ == '__main__':
		main()
	else:
		exit()

def identify(mac):
	if len(mac) == 17 or len(mac) == 12:
		# Requests data from https://macvendors.co/api/<MAC ADDRESS HERE> and loades response in obj
		request = urllib.Request(url+mac, headers={'User-Agent' : 'API Browser'})
		response = urllib.urlopen(request)
		obj = json.load(response)
		
		# Prints out obj
		sys.stdout.write(CYAN)
		print('\nCompany: ', obj['result']['company'])
		print('Address: ', obj['result']['address'])
		print('Type: ', obj['result']['type'],)
		print('MAC Prefix: ', obj['result']['mac_prefix'])
		print('Start HEX: ', obj['result']['start_hex'])
		print('End HEX: ', obj['result']['end_hex'], '\n')
		sys.stdout.write(RESET)
		
		if __name__ == '__main__':
			main()
		else:
			exit()
	else:
		invalid()


def main():
	try:
		# Ask for user input and passes the input to identify function
		sys.stdout.write(GREEN)
		mac = input("[+] Enter MAC Address: ")
		sys.stdout.write(RESET)
		identify(mac)
	except:
		sys.stdout.write('\n')
		exit()

if __name__ == '__main__':
	main()