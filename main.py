#!/usr/bin/python
# -*- coding: utf-8 -*-
colors=['\033[0m',   # 0}  WHITE
		'\033[31m',  # 1}  RED
		'\033[32m',  # 2}  YELLOW
		'\033[33m',  # 3}  PURPLE
		'\033[34m',  # 4}  CYAN
		'\033[35m',  # 5}  MAGENT
		'\033[36m',  # 6}  CURL ____
		'\033[1m',   # 7}  WHITE LOW
		'\033[4m',   # 8}  WHITE HIGH
		'\033[0m',   # 9}  WHITE (FUCK)
		'\033[40m',  # 10} BACKGROUND GREY
		'\033[41m',  # 11} BACKGROUND RED
		'\033[42m',  # 12} BACKGROUND GREEN
		'\033[43m',  # 13} BACKGROUND YELLOW
		'\033[32m']   # 14}  GREEN

import os, sys, time, readline, rlcompleter, os.path, platform, re, socket, glob, subprocess
from time import sleep
from sys import stdout, exit
from core import help
from core import header
from os.path import join
from subprocess import check_output
from lxml import etree
from core import retarget

def Command_exe(msg,cmd):
    	i = "\033[1mSTATUS"+colors[0]+":[Processing]"
	stdout.write(" " + msg + " %s" % i)
	stdout.flush()
	if subprocess.call(cmd+' >/dev/null 2>&1', shell=True)==0:
		i = "[\033[1m"+colors[14]+"OK"+colors[0]+"]"
	else:
		i = "["+colors[1]+"\033[1mERROR"+colors[0]+"]["+colors[0]+"\033[1mWARNING"+colors[0]+"]"

	stdout.write("\r " + msg +" STATUS:%s" % i)

os.system('clear')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Checking for Version Update                    ",'git clone https://github.com/DarkSpiritz/DarkSpiritz.git')
print "Updated"
os.system('clear')
version_open = open("storage/version","r")
version = version_open.read()
intname = "DARK"
lan_ip = os.popen("hostname -i | awk {' print $1 '}").read()

def complete(text, state):
    a = (glob.glob(text + '*') + [None])[state].replace("__init__.pyc", "").replace("__init__.py", "").replace(".plugin", "").replace("banners", "").replace("Resources", "").replace("storage", "").replace("modules", "").replace("plugin_support.py", "").replace("plugin_support.pyc", "").replace("core", "").replace("main.py","").replace("files","")
    a = a.replace("//", "/")
    if os.path.isfile(a[:-1] + ".py"):
        return a[:-1]
    else:
        return a

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

LOGS = "storage/logs"
STORAGE = "storage"
MODULES = "modules"
CORE = "core"
CHECK_LOGS = os.path.exists(LOGS)
CHECK_STORAGE = os.path.exists(STORAGE)
CHECK_MODULES = os.path.exists(MODULES)
CHECK_CORE = os.path.exists(CORE)
header.main_header()
if CHECK_CORE == False:
    print "Missing files..."
    sys.exit()
else:
    pass

if CHECK_MODULES == False:
    print "Missing files..."
    sys.exit()
else:
    pass

if CHECK_STORAGE == False:
    print "Missing files..."
    sys.exit()
else:
    pass

RescoursesDir = os.getcwd()
dandtime = time.strftime("%d-%m-%Y-%H:%M:%S")
logfile = "storage/logs/%s.log" % (dandtime)

if CHECK_LOGS == True:
    if os.path.exists("storage/logs/config.xml") == False:
        print "[" + time.strftime("%H:%M:%S") + "] Failed to load Configuration file.            STATUS:[" + colors[1] + "FAILED" + colors[0] + "]"
	os.system("cp storage/config-skeleton.xml storage/logs/config.xml")
	retarget.edit()
    print "[" + time.strftime("%H:%M:%S") + "] Creating a Configuration file: storage/logs/config.xml.            STATUS:[" + colors[14] + "OK" + colors[0] + "]"
    time.sleep(0.6)
else:
    print "[" + time.strftime("%H:%M:%S") + "] Failed creating Configuration file.            STATUS:[" + colors[1] + "FAILED" + colors[0] + "]"
    exit()

print "[" + time.strftime("%H:%M:%S") + "] Checking updates."
time.sleep(0.5)
print ""
#Wait and check internet activity
time.sleep(0.8)
sx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = '0.0.0.0'
try:
    sx.connect(('8.8.8.8', 80))
    hostname = sx.getsockname()
    data = "%s" % (hostname[0])
    print "   [" + colors[4] + "info" + colors[0] + "] Connected to a network", data
except KeyboardInterrupt:
    print "   [" + colors[1] + "info" + colors[0] + "] Failed to connect to a network"

#Start screen
time.sleep(0.1)
print "   [" + colors[4] + "info" + colors[0] + "] Initializing Global State."
time.sleep(0.6)
print "   [" + colors[4] + "info" + colors[0] + "] Detected Version => %s" % (version)
time.sleep(0.1)
mac_address = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read()
gateway_ip = check_output("/sbin/ip route | awk '/default/' | awk {' print $3 '} | sed -n 1p", shell=True)
PLUGIN_END = ".plugin"
PLUGIN_EXEC = "/usr/bin/python2 "

def main():
    try:
	line_1 = " [\033[31m" + intname + "\033[0m]\033[0m: "
	terminal = raw_input(line_1)
        if terminal[0:3] =='use':
            if terminal[4:] == terminal[4:]:
                Exploit_check = "%s.plugin" % (terminal[4:])
                if os.path.exists(Exploit_check) == True:
                   os.system("python %s.plugin" % (terminal[4:]))
                   main()
                else:
                    print "[\033[1;91m!\033[0m] %s: could not be found" % (terminal[4:])
        if terminal[0:6] == 'pyexec':
            exec(terminal[7:])
            main()
        elif terminal[0:21] == "retarget":
             retarget.edit()
             main()
        elif terminal[0:17] == 'show ' + terminal[5:]:
            print ""
            print "Plugin Category: " + terminal[5:]
            print "==============================\n"
            print " Name              Description"
            print " ----              -----------"
            directory_list = glob.glob(terminal[5:] + '/*.plugin')
            for line in directory_list:
                about = line
                with open(about, 'r') as myfile:
                    data = myfile.read().splitlines()
                    desc = data[0]
                    datar = desc.replace("Description = '", "")
                x = datar.rstrip("'")
                bb = line.split(terminal[5:] + '/')[1].split('.plugin')[0]
                if x == "#!/usr/bin/python":
                    x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
                print " %s\t   %s" % (bb,x)
            print " "
            main()
	elif terminal[0:] == 'session':
             print """Automatic Settings
======================

  Variable          Value
  --------          -----
  LOCAL_IP          %s  GATEWAY_IP        %s  MAC_ADDR          %s""" % (str(lan_ip), str(gateway_ip), str(mac_address))
             sesread = open("modules/session.py","r").read()
             print ""
             exec(sesread)
	     main()
        elif terminal[0:4] =='help':
            help.help()
            main()
        elif terminal[0:] == 'show':
            showlist()
            main()
        elif terminal[0:2] =='?':
            help.help()
            main()
        elif terminal[0:5] =='ipnet':
            os.system('ifconfig')
            main()
        elif terminal[0:5] =='clear':
            os.system('clear')
            main()
        elif terminal[0:6] =='banner':
            os.system('clear')
            header.main_header()
            main()
        elif terminal[0:9] =='exit':
            exit()
	elif terminal[0:1] =='!':
	    os.system(terminal[1:])
            main()
        else:
            print "[\033[1;94m?\033[0m] %s: command not found" % (terminal)
            main()
    except(KeyboardInterrupt):
        print "\n"
        return main()

def showlist():
    print """
Plugin Category
===============

 Name
 ----"""
    for d in glob.iglob('*'):
		if "lib" not in d:
			if "installer.py" not in d:
				if "main.py" not in d:
					if "banners" not in d:
						if "core" not in d:
							if "Resources" not in d:
								if "storage" not in d:
									if "modules" not in d:
										print """ %s""" % (d)
    print ""

if __name__=='__main__':
    main()
