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
        #print 'hello'
	 print os.system('sudo  qemu-img   create -f  qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2  /var/lib/libvirt/images/'+os_name+'.qcow2')
	 print os.system('sudo  virt-install  --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2  --import --noautoconsole --graphics=vnc,listen=192.168.10.235,port=5993,password=redhat1')
	 print os.system('sudo websockify --web=/usr/share/novnc 7096 192.168.10.235:5993')
         print os.system('sudo qr "192.168.10.235:7096" > /var/www/html/pic.png')
	#print os.system('sudo chmod +x /var/www/html/pic4.png')
var='''
     <html>
     <body>
     <a href ="../pic.png">click please</a>
     </body>
     </html> 
    '''
print var

