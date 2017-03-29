#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

def send_email(FROM,TO,SUBJECT,MSG):
	msg_file = open(MSG, "r")
	msg = MIMEText(msg_file.read())
	msg_file.close()
	msg['Subject'] = SUBJECT
	msg['From'] = FROM
	msg['To'] = TO

	s = smtplib.SMTP('localhost')
	s.sendmail(FROM, TO, msg.as_string())
	s.quit()
