#!/bin/env python

import subprocess
import re
import getpass
import time
#from optparse import OptionParser
import argparse

import sendGmail

def findProcess( processName ):
    argument1 = '-u' + ' ' + getpass.getuser()
    command = "pgrep %s %s" % (argument1, processName)
    ps= subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    return output

def isProcessRunning( processId):
    output = findProcess( processId )
    print output
    if output:
        return True
    else:
        return False

def runProcessWait( command ):
    ps = subprocess.Popen(command, shell=True)
    retVal = ps.wait();
    if retVal is None:
        return "Error, process hasn't terminated yet!"
    return retVal

if __name__ == "__main__":

    #parser = OptionParser()
    #parser.add_option("-f", "--find", action="store", type="string", dest="processName",
    #        default="", help="the process name you want to find and wait")
    #parser.add_option("-c", "--command", action="store", type="string", dest="command",
    #        default="", help="the command you want to run and wait")
    #parser.add_option("-m", "--mail", action="store_true", dest="sendMail",
    #        default=False, help="send email flag")

    #(options, args) = parser.parse_args()

    #command = options.command
    #processName = options.processName
    #sendMail = options.sendMail

    parser = argparse.ArgumentParser()
    parser.add_argument('--find', '-f', dest='processName', action='store',
            help='the process name you want to find and wait')
    parser.add_argument('--command', '-command', dest='command', action='store',
            help='sum the integers (default: find the max)')
    parser.add_argument('--mail', '-m', dest='sendMail', action='store_true',
            default=False, help='sum the integers (default: find the max)')
    args = parser.parse_args()

    command = args.command
    processName = args.processName
    sendMail = args.sendMail

    if command and processName:
        print "-f and -c option cannot coexist, please check!"
        exit(1)


    if command: 
        retVal = runProcessWait(command) 
        if retVal is not 0:
            print "error %d, run %s" % (retVal, command)

    if processName:
        running = True
        while True:
            running = isProcessRunning(processName)
            if not running:
                break;
            time.sleep(20)

    print "process finished!"

    if sendMail:
        username = ""
        password = ""
        destination = "lirenlin@gmail.com"
        tittle = "synthesis finished"
        message = "please check the sythesis result"
        param = (username, password, destination, tittle, message)

        sendGmail.sendMail(*param)
