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
		
		# Requests data from https://macvendors.co/api/<MAC ADDRESS HERE>
		request = urllib.Request(url+mac, headers={'User-Agent' : 'API Browser'})
		response = urllib.urlopen(request)
		
		# Reads the json response to obj with codec utf-8
		# reader = codecs.getreader('utf-8')
		obj = json.load(response)
		
		# Prints out the results in obj
		print('\nCompany: ', obj['result']['company'])
		print('MAC Prefix: ', obj['result']['mac_prefix'])
		print('Address: ', obj['result']['address'])
		print('Start HEX: ', obj['result']['start_hex'])
		print('End HEX: ', obj['result']['end_hex'])
		print('Country: ', obj['result']['country'])
		print('Type: ', obj['result']['type'], '\n')
		
		if __name__ == '__main__':
			main()
		else:
			exit()
	else:
		invalid()


def main():
	try:
		# Ask for user input and passes the input to identify function
		mac = input("[+] Enter MAC Address: ")
		identify(mac)
	except:
		sys.stdout.write(YELLOW)
		print('\n[x] Exiting...')
		sys.stdout.write(RESET)
		exit()

if __name__ == '__main__':
	main()