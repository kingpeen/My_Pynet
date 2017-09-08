#!/usr/bin/env python

'''
class based solution
'''


import telnetlib
import time
import socket
import sys
import getpass


TELNET_PORT = 23
TELNET_TIMEOUT = 6


class TelnetConn(object):
	'''
	Establish and manage telnet connection to network devices
	'''

	def __init__(self, ip_addr, username, password):
		self.ip_addr = ip_addr
		self.username = username
		self.password = password


		try:
			self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
		except:
			sys.exit("Connection timed Out")



	def login(self):
		'''
		Login to network device
		'''

		output = self.remote_conn.read_until("Username:", TELNET_TIMEOUT)
		self.remote_conn.write(self.username + '\n')
		output += self.remote_conn.read_until("Password:", TELNET_TIMEOUT)
		self.remote_conn.write(self.password + '\n')
		time.sleep(1)
		return output



 	def send_command(self, cmd = '\n', sleep_time=1):
		'''
		Send a command down the telnet channel
		'''
		cmd = cmd.rstrip()
		self.remote_conn.write(cmd + '\n')
		time.sleep(sleep_time)
		return self.remote_conn.read_very_eager()


	def disable_paging(self, paging_cmd='terminal leng 0'):
		'''
		Disable the paging of output
		'''

		return self.send_command(paging_cmd)

	
	def close_conn(self):
		'''
		Close telnet connection
		'''

		self.remote_conn.close()



def main():
	''' convert the code to class based solution '''
	ip_addr = raw_input("IP address:")
	ip_addr = ip_addr.strip()
	username = 'test'
	password = getpass.getpass()


	my_conn = TelnetConn(ip_addr, username, password)
	my_conn.login()
	my_conn.send_command()
	my_conn.disable_paging()
	output = my_conn.send_command('show ip int brief')

	print "\n\n"
	print output
	print "\n\n"


	my_conn.close_conn()


if __name__ == "__main__":
	main()
