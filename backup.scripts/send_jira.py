#!/usr/bin/env python

import subprocess
from shutil import copyfile
import os

size = os.path.getsize('/root/error.msg')
TEMPLATE = '/root/jira.template'
JSON = '/root/jira.file'

def send_jira(PROJ,SUMM,DESC):
	if ( size > 0 ):
		copyfile(TEMPLATE, JSON)
		TEXT = open(JSON).read()
		open(JSON,'w').write(TEXT.replace('PROJECT',PROJ).replace('SUMMARY',SUMM))
		bash_curl_send_jira = '/root/send_jira.sh'
		subprocess.call(bash_curl_send_jira, shell=True)
