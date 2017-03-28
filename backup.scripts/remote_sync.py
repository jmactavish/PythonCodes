#!/usr/bin/env python
#Author John Mactavish AKA Soap Mar28 2017

import subprocess
from os import system

def bash_rsync(LOG,SRC,DEST):
	rsync = 'rsync -avze "ssh -o StrictHostKeyChecking=no" --delete --log-file=' + LOG + ' ' + SRC + ' ' + DEST
	subprocess.call(rsync, shell=True)

def check_log(LOG):
	log_file = open(LOG, "r")
	for line in log_file:
		if 'err' in line:
			print line
		elif 'ERR' in line:
			print line
		else:
			break
	log_file.close()

