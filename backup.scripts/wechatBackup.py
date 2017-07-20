#!/usr/bin/env python

from backupLib import rsync,checkLog,sendMail,tarGz
from time import strftime
import os
import yaml

Yaml = 'wechatConf.yml'

with open(Yaml,'r') as yamlFile:
	conf = yaml.load(yamlFile)
	address = conf['address']
	log = address['dest'] + 'logs/' + strftime("%Y%m%d%H") + '.rsync.log'
	mail = conf['mail']
	source = address['src']
	sourceList = source['php'] + ' ' + source['db']

rsync(sourceList,address['dest'],address['port'],log)

checkLog(log,conf['err'])
	
sendMail(mail['from'],mail['receiver'],mail['summary'],log)

fileIn = address['dest'] + 'vnet'
fileOut = fileIn + '-' + strftime("%Y%m%d%H") + '.tar.gz'

tarGz(fileIn,fileOut)
