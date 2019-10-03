#!/usr/bin/python2

import socket
re_ip="172.31.10.223"
re_port=4484  # 0 - 1024 -- you can check free udp port : netstat -nulp

# Creating UDP socket
#		  ip type v4	   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


print '1. text communication \n 2.file transfer'
option = input('Choose an option: ')
if option == 1:
    print "To close communication send an blank message"
    # Sending data to target
    while(True):
    	text = raw_input('Server says: ')
    	if len(text) > 150:
    		print("Message limit exceeded")
    	else:
    		s.sendto(text,(re_ip,re_port))
    		data = s.recvfrom(100)
    		if len(data[0]) == 0:
    			s.sendto('',(re_ip,re_port))
    			break
    		print 'Client says: '+data[0]
    		re_ip,re_port = data[1]
    s.close()
elif option == 2:
    print "To close communication send an blank message"
    # Sending file to target
    while(True):
    	file_name = raw_input('Enter file name to send: ')
    	if len(file_name) == 0:
    		s.sendto('',(re_ip,re_port))
    		break
    	f = open(file_name)
    	s.sendto(f.read(),(re_ip,re_port))

    s.close()
