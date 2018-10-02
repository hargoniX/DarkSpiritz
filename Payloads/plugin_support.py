#!/usr/bin/python
import sys, os
import os.path
RescoursesDir = os.getcwd() + "/modules"

sys.path.insert(0, RescoursesDir)
from dave import *
import logging

dashboard()
