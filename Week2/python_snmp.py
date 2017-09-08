#!/usr/bin/env python

'''
Create a script that connects to both router and prints out the MIB2 sysName and sysDescr
'''

import getpass
import snmp_helper


SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():

	'''
	Create a script that connects to router and prints output
	'''

	ip_addr = raw_input("IP_address:")

	community_string = getpass.getpass(prompt='Community string:')

	router1 = (ip_addr, community_string, 161)


	print "\n***************"
	for the_oid in (SYS_NAME, SYS_DESCR):
		snmp_data = snmp_helper.snmp_get_oid(router1, oid = the_oid)
		output = snmp_helper.snmp_extract(snmp_data)
		print output

		print "*************************"
	print


if __name__ == "__main__":
	main()


		
