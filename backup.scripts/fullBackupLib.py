#!/usr/bin/env python

import subprocess
import os
from time import strftime

def bashRsync(src,dest,port):
	destDir = dest + strftime("%Y%m%d-%H%M") + '/'
	log = destDir + '/rsync.log'
	rsync = 'rsync -avze "ssh -o StrictHostKeyChecking=no -p' + port +  '" --log-file=' + log + ' ' + src + ' ' + destDir
	subprocess.call(rsync, shell=True)

def checkLog(LOG,ERR_FILE):
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
