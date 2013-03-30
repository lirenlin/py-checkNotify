#!/bin/env python
import smtplib  
from optparse import OptionParser
import getpass
import os
import sys

def sendMail(username='', password='', destination='', message='', tittle=''):
    print "-"*11,"Send Mail","-"*11

    if not username:
        username = raw_input("Please enter your username: ")
    if not password:
        password = getpass.getpass(prompt="Please enter your password: ")
    if not destination:
        destination = raw_input("Please enter the receiver's e-mail address: ")
    if not tittle:
        tittle = raw_input("Please enter the tittle of e-mail: ")
    if not message:
        print("Please enter the message body(finish with Ctrl-d)")
        while True:
            try:
                message += raw_input()
                message += os.linesep
            except EOFError:
                print "********Message edit done*********"
                break

    message = "Subject: %s\n\n%s" % (tittle, message)
    fromaddr = 'lirenlin@gmail.com'  
    toaddrs  = destination

    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()
    print "-"*4,"Mail has been delivered","-"*4

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-u", "--user", action="store", type="string", dest="username",
            default="", help="the username to login")
    parser.add_option("-p", "--password", action="store", type="string", dest="password",
            default="", help="the password of the account")
    parser.add_option("-d", "--destination", action="store", type="string", dest="destination",
            default="", help="the e-mail receiver's address")
    parser.add_option("-t", "--tittle", action="store", type="string", dest="tittle",
            default="", help="the tittle of the e-mail")
    parser.add_option("-m", "--message", action="store", type="string", dest="message",
            default="", help="the body message of the e-mail")

    (options, args) = parser.parse_args()

    # Credentials (if needed)  
    username = options.username
    password = options.password

    destination = options.destination
    tittle = options.tittle
    message = options.message

    sendMail(username, password, destination, message, tittle)

