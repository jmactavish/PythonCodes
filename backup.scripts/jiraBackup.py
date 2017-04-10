#!/usr/bin/env python

from backupLib import incrementalRsync,checkLog,sendMail
from time import strftime
import os
import yaml

Yaml = '/home/backup_robot/PythonCodes/backup.scripts/jiraConf.yml'

with open(Yaml,'r') as yamlFile:
	conf = yaml.load(yamlFile)
	address = conf['address']
	log = address['dest'] + 'logs/' + strftime("%Y%m%d-%H%M") + '.rsync.log'
	mail = conf['mail']
	source = address['src']
	sourceList = source['index'] + ' ' + source['attachment'] + ' ' + source['archive']

incrementalRsync(sourceList,address['dest'],address['port'],log)

checkLog(log,conf['err'])
	
sendMail(mail['from'],mail['receiver'],mail['summary'],log)
