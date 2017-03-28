#!/usr/bin/env python
#Author John Mactavish AKA Soap Mar28 2017

import subprocess

def bash_rsync (LOG,SRC,DEST):
	bash_rsync = 'rsync -avze "ssh -o StrictHostKeyChecking=no" --delete --log-file=' + LOG + ' ' + SRC + ' ' + DEST
	subprocess.call(bash_rsync, shell=True)

def check_log (LOG):
	log_file = open(LOG,"r")
	for line in log_file:
		if 'err' in line:
			print line
		if 'ERR' in line:
			print line
	log_file.close()
