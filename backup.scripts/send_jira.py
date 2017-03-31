#!/usr/bin/env python

import subprocess
from shutil import copyfile
import os

ERROR = '/root/error.msg'
err_size = os.path.getsize(ERROR)
TEMPLATE = '/root/jira.template'
JSON = '/root/jira.file'

def send_jira(LOG,PROJ,SUMM):
	if not os.path.exists(LOG):
		copyfile(TEMPLATE, JSON)
		JIRA = open(JSON,'r')
                TEXT = JIRA.read()
                open(JSON,'w').write(TEXT.replace('PROJECT',PROJ).replace('SUMMARY',SUMM).replace('DESCRIPTION','xps rsync didnt work last night!'))
                JIRA.close()
                bash_curl_send_jira = '/root/send_jira.sh'
                subprocess.call(bash_curl_send_jira, shell=True)
	if ( err_size > 0 ):
		error = open(ERROR, 'r')
		TEXT = error.read()
		DESC = TEXT.replace("\n","\\n").replace('\"','')
		error.close()
		copyfile(TEMPLATE, JSON)
		JIRA = open(JSON,'r')
		TEXT = JIRA.read()
		open(JSON,'w').write(TEXT.replace('PROJECT',PROJ).replace('SUMMARY',SUMM).replace('DESCRIPTION',DESC))
		JIRA.close()
		bash_curl_send_jira = '/root/send_jira.sh'
		subprocess.call(bash_curl_send_jira, shell=True)
