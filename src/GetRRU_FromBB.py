# -*- coding: utf-8 -*-
def Term():
	open('RRUS.log','w').close()	 #clear RRUS.log
	from subprocess import Popen
	args="amosbatch -p 2 listBS1.txt 'lt all;rbs;RBSEricsson12#;l+ RRUS.log; get rru prod; l-;'"	
	process=Popen(args, shell=True)
	process.wait()


def GetIn():
	f=open('RRUS.log')
	for line in f:
		if 'CH' in line:
			print line.split('>')[0]
		elif 'productName' in line:
			#print line.split(' ')[4].rstrip()
			print line.split('=')[1].rstrip()
		elif 'serialNumber' in line:
			#print line.split(' ')[4].rstrip()
			print line.split('=')[1]	

Term()
GetIn()


#amosbatch -p 1 cli/listBS1.txt 'lt all;l+ cli/Equipment.log; get . itt; get . ctna; l-;'
