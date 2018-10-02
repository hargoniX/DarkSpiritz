#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import string
import time
import random
import os
import glob
from lxml import etree
from urlparse import urlparse
from struct import pack
import rlcompleter, readline
import subprocess
from sys import stdout
from subprocess import check_output
XML = "storage/logs/config.xml"
tree = etree.parse(XML)

class colors:
    W  = '\033[0m'
    R  = '\033[31m'
    G  = '\033[32m'
    O  = '\033[33m'
    B  = '\033[34m'
    P  = '\033[35m'
    C  = '\033[36m'
    GR = '\033[40m'
    GY = '\033[43m'
    GE = '\033[41m'
    GW = '\033[4m'
    HH = '\033[1m'

intname = "\033[4m" + "dark"
det = sys.argv[0]
den = det.split('.')[-2]
fin = den.split('/')[1]
__plugin__      = "%s.plugin" % (fin)
RescoursesDir = os.getcwd()
dandtime = time.strftime("%H:%M:%S")

tabcomp = ['help','execute','info','back']

def completer(text, state):
    options = [x for x in tabcomp if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

def dashboard():
    try:
        line_1 = "+[\033[1m" + intname + "\033[0m](\033[31m" + fin + "\033[1;m): "
        terminal = raw_input(line_1).lower()
        time.sleep(0.2)
        if terminal == 'help':
            print "Core Commands"
            print "============="
            print ""
            print "  Command         Description"
            print "  -------         -----------"
            print "  help            Display help menu."
            print "  execute         Execute the plugin."
            print "  back            Go back."
            print "  info            Display module menu."
            print "  clear           Clear Terminal Cache."
            print ""
            dashboard()
        elif terminal == 'execute':
            before_execute()
            pass
        elif terminal == 'clear':
            os.system('clear')
            dashboard()
        elif terminal == "info":
            with open(den + ".plugin", 'r') as myfile:
                data = myfile.read().splitlines()
                desc = data[0]
                datar = desc.replace("Description = '", "")
                x = datar.rstrip("'")
                if x == "#!/usr/bin/python":
                    x = "[\033[1;31m?\033[0m] Description has not yet been implemented."
                print "Description: " + x
            dashboard()
        elif terminal == 'back':
            sys.exit()
        else:
            print "Unknown syntax: %s" % (terminal)
            dashboard()
    except KeyboardInterrupt:
        sys.exit()

class ask():
    tree = etree.parse("storage/logs/config.xml")
    for b in tree.xpath("/configuration/config/*"):
        dat = "%s = '%s'" % (b.tag,b.text)
	exec(dat)

def before_execute():
    try:
        default10 = "yes"
        time.sleep(0.2)
        print "[\033[1;94m?\033[0m] Configuring Plugin"
        time.sleep(1)
	print ""
        print "Name             Set Value"
        print "----             ----------"
	tree = etree.parse("storage/logs/config.xml")
	for d in tree.xpath("/configuration/config/*"):
            print "%s           %s" % (d.tag,d.text)
        print "Plugin           %s" % (fin)
        print ""
        et = raw_input("[\033[1;94m?\033[0m] Execute Plugins? [" + default10 + "]: ")  or default10
        if et == 'yes':
            pass
        elif et == 'no':
            exit()
        else:
            print "[\033[1;31m!\033[0m] No options were chosen."
    except KeyboardInterrupt:
        exit()

def run(cmd):
    x = check_output(cmd, shell=True)
    i = "[\033[1m"+colors.G+"!"+colors.W+"] "
    print i + x

def warning(msg):
    print "[\033[1m"+colors.O+"/"+colors.W+"]", msg

def fail(msg):
    print "[\033[1m"+colors.R+"!"+colors.W+"]", msg

def success(msg):
    print "[\033[1m"+colors.G+"*"+colors.W+"]", msg

def text(msg):
    print "[\033[1;94m*\033[0m]", msg
