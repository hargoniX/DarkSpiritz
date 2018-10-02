#!/usr/bin/env python
import os
import random

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

def main_header():
	ban = random.choice(os.listdir("banners"))
	banextenstion = "banners/%s" % (ban)
	ban_open = open(banextenstion, "r")
	print colors[5] + ban_open.read() + "\033[0m"
	ban_open.close()
