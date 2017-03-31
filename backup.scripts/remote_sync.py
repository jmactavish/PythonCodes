#!/usr/bin/env python
#Author John Mactavish AKA Soap Mar28 2017
#this script defines rsync & record errors into error log file

import subprocess
import os

def bash_rsync(LOG,SRC,DEST):
	rsync = 'rsync -avze "ssh -o StrictHostKeyChecking=no" --log-file=' + LOG + ' ' + SRC + ' ' + DEST
	subprocess.call(rsync, shell=True)

def check_log(LOG,ERR_FILE):
	if os.path.exists(LOG):
		log_file = open(LOG, "r")
		err_file = open(ERR_FILE, "a")
		open(ERR_FILE,"w").close()
		for line in log_file:
			if 'err' in line:
				err_file.write(line)
			if 'ERR' in line:
				err_file.write(line)
			if 'fail' in line:
				err_file.write(line)
		log_file.close()
		err_file.close()
