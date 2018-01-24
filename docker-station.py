#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands
import cgitb

cgitb.enable()

HOST = '192.168.36.16'

print "Content-type: text/html"
print "\r\n"
print "<html>"

print "<head>"
print "<title>DockerStation@{0}</title>".format(HOST)
print "</head>"

print "<body>"

containers = commands.getoutput("docker ps --format \"{{.Names}}\"").split()

print "<h1>Docker Station</h1>"
print "<ul>"

for c in sorted(containers):

    print "<li>"
    print c

    url = commands.getoutput("docker exec {0} /bin/bash -c \"jupyter notebook list\"".format(c))
    url = url.strip()
    url = url.strip("Currently running servers: ")
    url = url.split("::")[0]
    
    ports = commands.getoutput("docker container port {0}".format(c))
    ports = ports.replace('tcp -> 0.0.0.0:', '')
    ports = ports.strip()
    maps = ports.split()
    
    for m in maps: 
        p_container, p_host = m.split('/')
        if p_container == '8888': 
            print "<a href=\""
            print url.replace('localhost', HOST).replace('8888', p_host)
            print "\">"
            print p_host
            print "</a>"
        
    print "</li>"
    #print "<BR>"

print "</ul>"
print "</body>"
print "</html>"

print "</html>"
