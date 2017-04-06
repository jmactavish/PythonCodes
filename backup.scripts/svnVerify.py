#!/usr/bin/env python

import yaml
import os
from time import strftime
from jira import JIRA

with open('svnConf.yaml','r') as yamlFile:
        conf = yaml.load(yamlFile)
        address = conf['address']
	Jira = conf['jira']
	log = address['dest'] + 'logs/' + strftime("%Y%m%d-%H%M") + '.rsync.log'

jiraServer = JIRA(options={'server':Jira['addr'],'verify':False},basic_auth=(Jira['user'],Jira['pass']))

if not os.path.exists(log):
	print 'log doesnt exist'
	jiraServer.create_issue(project=Jira['project'],summary=Jira['summary'],description=Jira['desc'],issuetype={'name':'Bug'},assignee={'name':Jira['assign']})
elif (os.path.getsize(conf['err']) > 0 ):
	print 'error found'
	with open(conf['err'],'r') as errors:
		desc = errors.read()
		jiraServer.create_issue(project=Jira['project'],summary=Jira['summary'],description=desc,issuetype={'name':'Bug'},assignee={'name':Jira['assign']})
else:
	print 'safe'
