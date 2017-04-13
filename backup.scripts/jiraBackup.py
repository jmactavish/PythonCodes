#!/usr/bin/env python

from backupLib import rsync,checkLog,sendMail,tarGz
from time import strftime
import os
import yaml

Yaml = '/home/backup_robot/PythonCodes/backup.scripts/jiraConf.yml'

with open(Yaml,'r') as yamlFile:
	conf = yaml.load(yamlFile)
	address = conf['address']
	log = address['dest'] + 'logs/' + strftime("%Y%m%d%H") + '.rsync.log'
	mail = conf['mail']
	source = address['src']
	sourceList = source['index'] + ' ' + source['attachment'] + ' ' + source['archive']

rsync(sourceList,address['dest'],address['port'],log)

checkLog(log,conf['err'])
	
sendMail(mail['from'],mail['receiver'],mail['summary'],log)

attachmentsIn = address['dest'] + 'attachments'
attachmentsOut = attachmentsIn + '-' + strftime("%Y%m%d%H") + '.tar.gz'

tarGz(attachmentsIn,attachmentsOut)

indexIn = address['dest'] + 'indexes'
indexOut = indexIn + '-' + strftime("%Y%m%d%H") + '.tar.gz'

tarGz(indexIn,indexOut)
