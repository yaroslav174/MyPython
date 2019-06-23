# -*- coding: utf-8 -*-
def TermOSSCE():
	from subprocess import Popen
	args="/opt/ericsson/bin/cex_client"	
	process=Popen(args, shell=True)
	#process.wait()
	
def TermRNCE69():	
	
	import subprocess
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE069"']
	cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True)
	
		
def TermRNCE74():

	import subprocess
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE074"']
	cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True)

def TermRNCE131():

	import subprocess
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE131"']
	cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True)

def TermRNCE129():

	import subprocess
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE129"']
	cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True)

TermOSSCE()
TermRNCE69()
TermRNCE74()
TermRNCE129()
TermRNCE131()


