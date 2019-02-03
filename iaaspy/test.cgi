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

if  os_name ==  "redhat"  :
	#  a fresh copy 
	print  os.system('sudo  qemu-img   create -f  qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2  /var/lib/libvirt/images/'+os_name+'.qcow2')
	print os.system('sudo  virt-install  --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2  --import --noautoconsole --graphics=vnc,listen=192.168.10.165,port=5993,password=redhat1')
	print os.system('sudo websockify --web=/usr/share/novnc 7053 192.168.10.165:5993')
        print os.system('sudo qrencode -s 16*16 -o /myos.png 192.168.10.165:7053')
