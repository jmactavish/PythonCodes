#!/usr/bin/env python

import subprocess

import os
size = os.path.getsize('/root/error.msg')

def send_jira():
	if ( size > 0 ):
		bash_curl_send_jira = '/root/send_jira.sh'
		subprocess.call(bash_curl_send_jira, shell=True)
