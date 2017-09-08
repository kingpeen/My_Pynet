#! /usr/bin/env python

import telnetlib
import time


TELNET_PORT = 23
#time out in seconds
TELNET_TIMEOUT = 6

def main():
	ip_addr = "192.168.56.50"
	username = "test"
	password = "test"

	remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
#read until you match "username" in the output or it will timeout in 6 seconds
	output = remote_conn.read_until("Username:", TELNET_TIMEOUT)
	remote_conn.write(username + "\n")
	output = remote_conn.read_until("Password:", TELNET_TIMEOUT)
	remote_conn.write(password + "\n")
	

	time.sleep(1)
# read eager reads all output in non blocking way
	output = remote_conn.read_very_eager()
	
	
#Now we should be logged into the router. Lets send a command to route"
	remote_conn.write("terminal length 0" + "\n")
	time.sleep(1)
	output = remote_conn.read_very_eager()

	remote_conn.write("show run" + "\n")
	time.sleep(1)
	output = remote_conn.read_very_eager()
	
	print output

        remote_conn.close()

if __name__ == "__main__":
	main()
