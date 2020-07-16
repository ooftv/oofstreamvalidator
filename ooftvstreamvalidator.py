#!/usr/bin/python

import os, getopt, sys
from datetime import datetime
# =================================
# First try to get the stream health (is something streaming or not)
# =================================
# =================================
# Then try to see if the video server is playing videos
# =================================

# Default variables
testTime = 1
testURL = "https://www.ooftv.net/live/oof.m3u8"

# handle command line arguments (if any)
print '(sys.argv)=', (sys.argv)
print 'Number of arguments:', len(sys.argv), 'arguments.'
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "i:t:"
long_options = ["input", "time"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    print (str(err))
    sys.ext(2)

for current_argument, current_value in arguments:
    if current_argument in ("-i", "--input"):
        print ("input url detected:", current_argument, current_value)
        testURL = current_value
        print ("Current URL = ", testURL)
    elif current_argument in ("-t", "--time"):
        print ("time input detected:", current_argument, current_value )
        testTime = current_value
        print ("Current Time = ", testTime)


# First, get the stream raw data from Apple's mediastreamvalidator
# mediastream options:
# -t lets you set a time;
# -i is for immediate, useful for live streams
os.system('mediastreamvalidator -t ' + str(testTime) + ' ' + testURL)

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

# =================================
# check vlc log,
# do something if it can't read it or there's an error, fi
# find a cue in the log to have a heartbeat to track
