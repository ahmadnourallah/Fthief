#!/usr/bin/python3
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib, sys, argparse
from argparse import RawTextHelpFormatter
## color
Qblue = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
bgreen = '\033[93m'
red = '\033[91m'
white = '\033[0m'
bwhite = '\033[4m'
## parser
parser = argparse.ArgumentParser(prog="Fthief", usage="python3 Fthief [options]", add_help=True, epilog="e.x: python3 Fthief.py -u *****@gmail.com -p ***** -a /path/file\n     python3 Fthief.py -s smtp@server.com:port -u ***@server.com -p *** -a /path/file", formatter_class=RawTextHelpFormatter)
parser.add_argument('-v', '--version', action='version', version="""version 1.0, coded by Ahmad Nourallah""")
requ = parser.add_argument_group("# Require")
requ.add_argument('-u', '--username', dest='username', required=False, help="Used to enter password")
requ.add_argument('-p', '--password', dest='password', required=False, help="Used to enter user name")
requ.add_argument('-a', '--attachment', dest='attach', required=False, help='Used to select the attachment')
requ.add_argument('-tu', '--tusername', dest='tusername', required=False, help='Used to select mail to send attachment')
requ.add_argument('-s', '--server', dest='server', required=False, help='Used to select mail server default(smtp.gmail.com:587)',default='smtp.gmail.com:587')
args = parser.parse_args()
if len(sys.argv) < 2:
  print(red+'Error: '+white+"You must set argument")
  sys.exit(0)
#
try:
  print(white+'['+bgreen+'!'+white+']'+white+' Fthief --> '+"I'm on my way") 
  emaillist = str(args.tusername)
  msg = MIMEMultipart()
  msg['Subject'] = "it's delivering"
  msg['From'] = str(args.username)
  msg['Reply-to'] = str(args.tusername)
  msg.preamble = 'Multipart massage.\n'
  part = MIMEText("Sent by the Fthief tool you can download from here https://github.com/ahmadnourallah/Fthief")
  msg.attach(part)
  try: 
    part = MIMEApplication(open(str(args.attach),"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str(args.attach))
    msg.attach(part)
  except FileNotFoundError:
    print(red+'Error: '+white+"The file path doesn't exist")
    sys.exit(0) 	
  server = smtplib.SMTP(str(args.server))
  server.ehlo()
  server.starttls()
  try:
    server.login(str(args.username), str(args.password)) 
    server.sendmail(msg['From'], emaillist , msg.as_string())
  except smtplib.SMTPAuthenticationError:
    print(red+'Error: '+white+'Check your email or password and try again')
    sys.exit(0)
except KeyboardInterrupt:
  print(white+'\n['+bgreen+'!'+white+']'+white+' Fthief --> '+"Good Bye") 
