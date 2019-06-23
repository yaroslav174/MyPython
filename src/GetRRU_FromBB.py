# -*- coding: utf-8 -*-
def Term():
	open('RRUS.log','w').close()	 #clear RRUS.log
	from subprocess import Popen
	args="amosbatch -p 2 listBS1.txt 'lt all;rbs;RBSEricsson12#;l+ RRUS.log; get rru prod; l-;'" #amosbatch function for each value from file "list1.txt", execution some commands and write log
	process=Popen(args, shell=True)
	process.wait()


def GetIn():  						#search necessary parameters (type of RRUS(remote radio unit))
	f=open('RRUS.log')  			# open log
	for line in f:     				# concurrence string with "CH"
		if 'CH' in line:
			print line.split('>')[0] #print value more null
		elif 'productName' in line:  # for string with "productName"
			#print line.split(' ')[4].rstrip()
			print line.split('=')[1].rstrip() #print value from right side of "productName"
		elif 'serialNumber' in line: # for string with "serialNumber"
			#print line.split(' ')[4].rstrip()
			print line.split('=')[1] #print value from right side of "serialNumber"

Term()
GetIn()


#amosbatch -p 1 cli/listBS1.txt 'lt all;l+ cli/Equipment.log; get . itt; get . ctna; l-;'
