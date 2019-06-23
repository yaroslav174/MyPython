# -*- coding: utf-8 -*-
def TermOSSCE():
	from subprocess import Popen   				 #inport Popen for subprocess
	args="/opt/ericsson/bin/cex_client"		     #set path of application for var "args(argument)"
	process=Popen(args, shell=True)				 #open application
	#process.wait()
	
def TermRNCE69():								 #function for RNCE69
	
	import subprocess							
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE069"'] #path for terminal and command to open executable file
	#cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True) 								    #open terminal and run executable file "RNCE-CHE069" with a some comands
	
		
def TermRNCE74():

	import subprocess
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE074"']
	#cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True)

def TermRNCE131():

	import subprocess
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE131"']
	#cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True)

def TermRNCE129():

	import subprocess
	from subprocess import Popen
	cmd1 = ['/bin/gnome-terminal -e "/home/ytselk/cli/Python/RNCE-CHE129"']
	#cmd2 = 'lt all'
	a = subprocess.Popen(cmd1, shell=True)

TermOSSCE()  #sequence for functions
TermRNCE69()
TermRNCE74()
TermRNCE129()
TermRNCE131()


