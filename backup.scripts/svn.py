#!/usr/bin/env python

from time import strftime

LOG = "/data/dev_svn_backup/logs/" + strftime("%Y%m%d-%H%M") + ".log"
SRC = "backup_robot@util2:/var/svn"
DEST = "/data/dev_svn_backup/"
ERR_FILE = "/root/error.msg"

from remote_sync import bash_rsync
bash_rsync(LOG,SRC,DEST)
from remote_sync import check_log
check_log(LOG,ERR_FILE)

SUBJECT = 'SVN REPO BACKUP ' + strftime("%x,%X")
MSG = LOG
FROM = 'root@xps'
TO = open('/root/john.mail.list',"r").read()
#TO = '/root/john.mail.list'

from send_email import send_email
send_email(FROM,TO,SUBJECT,MSG)

from send_jira import send_jira
send_jira()
