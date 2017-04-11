#!/usr/bin/env python

from backupLib import noDelRsync,checkLog,sendMail
from time import strftime
import os
import yaml

Yaml = '/home/backup_robot/PythonCodes/backup.scripts/confluenceConf.yml'

with open(Yaml,'r') as yamlFile:
	conf = yaml.load(yamlFile)
	address = conf['address']
	log = address['dest'] + 'logs/' + strftime("%Y%m%d-%H%M") + '.rsync.log'
	mail = conf['mail']

noDelRsync(address['src'],address['dest'],address['port'],log)

checkLog(log,conf['err'])
	
sendMail(mail['from'],mail['receiver'],mail['summary'],log)
