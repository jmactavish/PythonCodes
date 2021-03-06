#!/usr/bin/env python

from backupLib import noDelRsync,checkLog,sendMail
from time import strftime
import os
import yaml

Yaml = 'svnConf.yml'

with open(Yaml,'r') as yamlFile:
	conf = yaml.load(yamlFile)
	address = conf['address']
	dest = address['dest']
        destDir = dest + strftime("%Y%m%d-%H%M") + '/'
        log = dest + 'logs/' + strftime("%Y%m%d-%H%M") + '.rsync.log'
	mail = conf['mail']

noDelRsync(address['src'],destDir,address['port'],log)

checkLog(log,conf['err'])
	
sendMail(mail['from'],mail['receiver'],mail['summary'],log)
