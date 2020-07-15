# oofstreamvalidator
Automate this script to monitor the oof live stream

Tips:

If you invoke it with the command only, this will work on the default oof steam url for 1 second. You can specify either a different URL and/or a different time length like this:

oofstreamvalidator.py -t 20 -i url.com/playlist.m3u8

This python script is just a wrapper for Apple's mediastreamvalidator tool which can be downloaded from developer.apple.command
Along with that tool comes another tool called hlsreport

When mediastreamvalidator is run, it generates a validation_data.json

Run:
hlsreport validation_data.json

To get an html report that tells you what's wrong with the stream
