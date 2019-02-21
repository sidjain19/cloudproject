#!/usr/bin/python2

import  cgi,cgitb,os,commands,time,subprocess
cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_name=web.getvalue('os')
os_ram=web.getvalue('ram')
os_cpu=web.getvalue('cpu')
os_hdd=web.getvalue('disk')

if  os_name ==  "redhat":
    commands.getoutput('sudo  qemu-img   create -f  qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2  /var/lib/libvirt/images/'+os_name+'.qcow2')
    commands.getoutput('sudo  virt-install --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2  --import --noautoconsole --graphics=vnc,listen=192.168.10.9,port=5993,password=redhat1')
    commands.getoutput('sudo websockify --web=/usr/share/novnc 9025 192.168.10.9:5993')
    commands.getoutput('sudo qr "192.168.10.9:9025" > /var/www/html/pic.png')


var1='''
 <!DOCTYPE html>
 <html>
 <body>
 <a href ="../pic.png">click please</a>
 </body>
 </html> 
'''
print var1


