#!/usr/bin/env python

from backupLib import noDelRsync,checkLog,sendMail
from time import strftime
import os
import yaml

Yaml = 'confluenceConf.yml'

with open(Yaml,'r') as yamlFile:
	conf = yaml.load(yamlFile)
	address = conf['address']
	logDir = address['dest'] + 'logs/'
	mail = conf['mail']

try:
    os.stat(logDir)
except:
    os.mkdir(logDir)

log = logDir + strftime("%Y%m%d") + '.rsync.log'

noDelRsync(address['src'],address['dest'],address['port'],log)

checkLog(log,conf['err'])
	
sendMail(mail['from'],mail['receiver'],mail['summary'],log)
