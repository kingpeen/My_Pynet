#! /usr/bin/env python

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
#time out in seconds
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
	cmd = cmd.rstrip()	
	remote_conn.write(cmd + "\n")
	time.sleep(1)
	return remote_conn.read_very_eager()

def login(remote_conn,username, password):
	
#read until you match "username" in the output or it will timeout in 6 seconds	
	remote_conn.read_until("Username:", TELNET_TIMEOUT)
	remote_conn.write(username + "\n")
	remote_conn.read_until("Password:", TELNET_TIMEOUT)
	remote_conn.write(password + "\n")
	time.sleep(1)
# read eager reads all output in non blocking way
	return remote_conn.read_very_eager()

def telnet_connect(ip_addr):
	try:
		return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	except socket.error:
		sys.exit("Connection error. Check if IP is valid or reachable")
	


def main():
	ip_addr = "192.168.56.50"
	username = "test"
	password = "test"
	
	remote_conn = telnet_connect(ip_addr)	
			
	login(remote_conn,username,password)
	
#Now we should be logged into the router. Lets send a command to route"
	output = send_command(remote_conn, "terminal length 0")
	output = send_command (remote_conn, "show ver")

	
	print output

        remote_conn.close()

if __name__ == "__main__":
	main()
