#!/usr/bin/python2
import commands
commands.getoutput("mkdir /mnt/samba/demo8 -p")
commands.getoutput("mount //192.168.10.9/demo8 /mnt/samba/demo8 -o username=taani,password=redhat")
