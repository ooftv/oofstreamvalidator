#!/bin/python

import os
from datetime import datetime


# First, get the stream raw data from Apple's mediastreamvalidator
# I still need the time and url to be inputtable

testTime = 1
testURL = "https://www.ooftv.net/live/oof.m3u8"
os.system('mediastreamvalidator -t ' + str(testTime) + ' ' + testURL)
# mediastream options:
# -t lets you set a time;
# -i is for immediate, useful for live streams

# get a timestamp for reference
timestamp = datetime.now()
print("The time is " + str(timestamp))

# Location to store the data
logfiles = "/tmp/"
logfilesdata = logfiles + "data/"
print(logfiles)
print(logfilesdata)

# todo: only make this folder if it doesn't exist
#os.makedirs(logfilesdata)

# move the outputted json file to the data directory
# os.rename("validation_data.json", str(logfilesdata) + str(timestamp) + "validation_data.json"
