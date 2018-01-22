#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands
import cgitb

cgitb.enable()

print "Content-type: text/html"
print "\r\n"
print "<html>"

print "<body>"

containers = commands.getoutput("docker ps --format \"{{.Names}}\"").split()

for c in sorted(containers):


    url = commands.getoutput("docker exec {0} /bin/bash -c \"jupyter notebook list\"".format(c))
    url = url.strip()
    url = url.strip("Currently running servers: ")
    #url = url.strip(" :: /notebook")
    url = url.split("::")[0]
    
    ports = commands.getoutput("docker container port {0}".format(c))
    ports = ports.replace('tcp -> 0.0.0.0:', '')
    ports = ports.strip()
    maps = ports.split()
    
    for m in maps: 
        p_container, p_host = m.split('/')
        print "<a href=\""
        print url.replace('localhost','192.168.100.33').replace('8888', p_host)
        print "\">"
    
        print "{0}::{1}".format(c, p_container)
        print "</a>"
        
        print "<BR>"

print "</body>"

print "</html>"
