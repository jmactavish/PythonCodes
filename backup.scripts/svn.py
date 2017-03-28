#!/usr/bin/env python

from time import strftime

LOG = "/data/dev_svn_backup/logs/" + strftime("%Y%m%d-%H%M%S") + ".log"
SRC = "backup_robot@util2.21vtech.com:/var/svn"
DEST = "/data/dev_svn_backup/"

from remote_sync import bash_rsync
bash_rsync(LOG,SRC,DEST)
from remote_sync import check_log
check_log(LOG)
