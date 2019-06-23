# -*- coding: utf-8 -*-
def Term():
	open('RRUS.log','w').close()	 #clear RRUS.log
	from subprocess import Popen
	args="amosbatch -p 2 listBS1.txt 'lt all;l+ RRUS.log; get . ctna; l-;'"	
	process=Popen(args, shell=True)
	process.wait()


def GetIn():
	f=open('RRUS.log')
	for line in f:
		if 'CH' in line:
			print line.split('>')[0]
		elif 'productName' in line and 'Aux' in line:
			print line.split('       ')[3].rstrip()


Term()
GetIn()


#amosbatch -p 1 cli/listBS1.txt 'lt all;l+ cli/Equipment.log; get . itt; get . ctna; l-;'
