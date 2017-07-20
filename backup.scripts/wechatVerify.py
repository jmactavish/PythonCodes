#!/usr/bin/env python

import yaml
import os
from time import strftime
from jira import JIRA

Yaml = 'wechatConf.yml'

with open(Yaml,'r') as yamlFile:
        conf = yaml.load(yamlFile)
        address = conf['address']
	Jira = conf['jira']
	log = address['dest'] + 'logs/' + strftime("%Y%m%d%H") + '.rsync.log'

jiraServer = JIRA(options={'server':Jira['addr'],'verify':False},basic_auth=(Jira['user'],Jira['pass']))

def sendJira(desc):
	jiraServer.create_issue(project=Jira['project'],summary=Jira['summary'],description=desc,issuetype={'name':'Bug'},assignee={'name':Jira['assign']})

fileIn = address['dest'] + 'vnet'
fileOut = fileIn + '-' + strftime("%Y%m%d%H") + '.tar.gz'

if not os.path.exists(log):
	sendJira(Jira['desc'])
elif (os.path.getsize(conf['err']) > 0 ):
	with open(conf['err'],'r') as errors:
		desc = errors.read()
		sendJira(desc)
elif os.path.exists(log):
	with open(log,'r') as Log:
		count = 0
		for line in Log:
			if 'sql' in line:
				count += 1
		print count
		if not ( count == 1 ):
			sendJira(Jira['dbErr'])
elif not os.path.exists(fileOut):
	sendJira(Jira['noArchive'])
