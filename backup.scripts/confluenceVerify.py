#!/usr/bin/env python
#pip install pyyaml jira

import yaml
import os
from time import strftime
from jira import JIRA

Yaml = 'confluenceConf.yml'

with open(Yaml,'r') as yamlFile:
        conf = yaml.load(yamlFile)
        address = conf['address']
	Jira = conf['jira']
	log = address['dest'] + 'logs/' + strftime("%Y%m%d") + '.rsync.log'

jiraServer = JIRA(options={'server':Jira['addr'],'verify':False},basic_auth=(Jira['user'],Jira['pass']))

def sendJira(desc):
	jiraServer.create_issue(project=Jira['project'],summary=Jira['summary'],description=desc,issuetype={'name':'Bug'},assignee={'name':Jira['assign']})

if not os.path.exists(log):
	sendJira(Jira['desc'])
elif (os.path.getsize(conf['err']) > 0 ):
	with open(conf['err'],'r') as errors:
		desc = errors.read()
		sendJira(desc)
else:
	print('safe')
