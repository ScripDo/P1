#!/usr/bin/python
#kris downs o_O



import os
import smtplib
import email
import ConfigParser




def getconfig(credpath):
    config = ConfigParser.ConfigParser()
    config.read(credpath)
    username = config.get('credentials', 'user')
    password = config.get('credentials', 'pwd')
    recipient = config.get('credentials', 'recipient')
    carboncopy = config.get('credentials', 'carboncopy')
    credlist=[username, password, recipient, carboncopy]
    return credlist

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.close()
    return problems

if __name__ == "__main__":

    credpath="/home/kris/configs/sendEmailTest.ini"

    credlist=getconfig(credpath)

    emailuser=credlist[0]
    emailpwd=credlist[1]
    emailrec=credlist[2]
    emailcc=credlist[3]

    sendemail(from_addr    = emailuser, 
              to_addr_list = [emailrec],
              cc_addr_list = [emailcc], 
              subject      = 'Test System Email', 
              message      = 'Testing \n', 
              login        = emailuser, 
              password     = emailpwd)


