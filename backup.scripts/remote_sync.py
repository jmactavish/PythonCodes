#!/usr/bin/env python
#Author John Mactavish AKA Soap Mar28 2017

import subprocess
from os import system

def bash_rsync(LOG,SRC,DEST):
	rsync = 'rsync -avze "ssh -o StrictHostKeyChecking=no" --delete --log-file=' + LOG + ' ' + SRC + ' ' + DEST
	subprocess.call(rsync, shell=True)

def check_log(LOG,ERR_FILE):
	log_file = open(LOG, "r")
	err_file = open(ERR_FILE, "a")
	open(ERR_FILE,"w").close()
	for line in log_file:
		if 'error' in line:
			err_file.write(line)
			print line
	log_file.close()
	err_file.close()
