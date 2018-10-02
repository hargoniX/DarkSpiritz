#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
from lxml import etree

def edit():
    time.sleep(0.1)
    XML = "storage/logs/config.xml"
    CHECK_XML = os.path.exists(XML)
    if CHECK_XML == False:
       os.system('cp storage/config-skeleton.xml storage/logs/config.xml')
    else:
       pass

    tree = etree.parse(XML)

    start = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
 <config name="ds">"""

    end = """</config>
</configuration>"""

    f = open(XML,"w")
    f.write(start)

    for l in tree.xpath("/configuration/config/*"):
        lhost = "%s" % (l.text)
        defer = raw_input("[\033[1;94m+\033[0m] Retarget '" + l.tag + "' [" + l.text + "]:") or l.text
        f.write("\n  <" + l.tag + ">" + defer + "</" + l.tag + ">")
    f.write(end)
    f.close()
