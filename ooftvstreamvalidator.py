#!/bin/python

import os

# First, get the stream raw data from Apple's mediastreamvalidator
# I still need to set the length as an adjustable validator, and the url to be inputtable

os.system('mediastreamvalidator -t 10 https://www.ooftv.net/live/oof.m3u8')
