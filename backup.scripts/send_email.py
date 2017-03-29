#!/usr/bin/env python

def send_email(FROM,TO,SUBJECT,MSG):
	import smtplib
	from email.mime.text import MIMEText
	msg_file = open(MSG, "r")
	msg = MIMEText(msg_file.read())
	msg_file.close()
	msg['Subject'] = SUBJECT
	msg['From'] = FROM
	msg['To'] = TO

	s = smtplib.SMTP('localhost')
	s.sendmail(FROM, TO, msg.as_string())
	s.quit()
