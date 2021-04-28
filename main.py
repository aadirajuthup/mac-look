import json
import urllib.request as urllib
import codecs
from os import system
from time import sleep

url = 'https://macvendors.co/api/'

ColorOff = "\\033[0m"
Red = "\\033[0;31m"

def identify(mac):
	# Checks if the input length is 17 or 12, if yes gets details if not ask input again or exit
	if len(mac) != 17 or len(mac) != 12:
		print('[-] Invalid MAC Address')
		sleep(3)
		if __name__ == '__main__':
			main()
		else:
			exit()
	else:
		# Requests data from https://macvendors.co/api/<MAC ADDRESS HERE>
		request = urllib.Request(url+mac, headers={'User-Agent' : 'API Browser'})
		response = urllib.urlopen(request)
		# Reads the json response to obj with codec utf-8
		reader = codecs.getreader('utf-8')
		obj = json.load(reader(response))
		# Prints out the results in obj
		print('Company: ', obj['result']['company'])
		print('MAC Prefix: ', obj['result']['mac_prefix'])
		print('Address: ', obj['result']['address'])
		print('Start HEX: ', obj['result']['start_hex'])
		print('End HEX: ', obj['result']['end_hex'])
		print('Country: ', obj['result']['country'])
		print('Type: ', obj['result']['type'])

def main():
	# Ask for user input and passes the input to identify function
	system('clear')
	mac = input("[+] Enter MAC Address: ")
	identify(mac)

if __name__ == '__main__':
	main()