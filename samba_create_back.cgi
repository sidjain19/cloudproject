#!/usr/bin/python2

import  cgi,cgitb,os,json,commands
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
st_name=web.getvalue('storage')
size=web.getvalue('size')
st_name=st_name.strip(' ')
size=size.strip(' ')
ip=web.getvalue('ip')
ip=ip.strip(' ')
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('select user_name from currentuser')
res=sql.fetchall()
user=[]
for i in res:
	user.append(json.dumps(i).strip('[""]'))

var1=commands.getstatusoutput('sudo lvcreate --name '+st_name+' --size '+size+' samba')
commands.getoutput('sudo mkfs.xfs /dev/samba/'+st_name)
commands.getoutput('sudo mkdir /smb_share/'+st_name)
var4=commands.getstatusoutput("sudo mount /dev/samba/"+st_name+" /smb_share/"+st_name)
commands.getoutput('sudo chmod 777 /smb_share/'+st_name)

var1=commands.getoutput('sudo echo /dev/samba/'+st_name+' /smb_share/'+st_name+'  xfs defaults 0  0 >> /etc/fstab ')

commands.getoutput('sudo echo ['+st_name+'] >> /etc/samba/smb.conf')
commands.getoutput('sudo echo path = /smb_share/'+st_name+' >> /etc/samba/smb.conf')
commands.getoutput('sudo echo browseable = yes >> /etc/samba/smb.conf')
commands.getoutput('sudo echo writeable = yes >> /etc/samba/smb.conf')
commands.getoutput('sudo echo write list = +taani >> /etc/samba/smb.conf')
commands.getoutput('sudo echo hosts allow = '+ip+' >> /etc/samba/smb.conf')


commands.getoutput('sudo chgrp taani /smb_share/'+st_name)
commands.getoutput('sudo chmod g+w /smb_share/'+st_name)
commands.getoutput('sudo iptables -F')
commands.getoutput('sudo setenforce 0')
commands.getoutput('sudo systemctl restart smb')
commands.getoutput('sudo systemctl enable smb')

fi=open('/var/www/html/shell/samba.sh',mode='w')
fi.write('#!/usr/bin/python2\n')
fi.close()

fi=open('/var/www/html/shell/samba.sh',mode='a')
fi.write('import commands\n')
fi.write('commands.getoutput("mkdir /mnt/samba/'+st_name+' -p")\n')
fi.write('commands.getoutput("mount //192.168.10.9/'+st_name+' /mnt/samba/'+st_name+' -o username=taani,password=redhat")\n')
fi.close()
sql.execute('insert into smb values(%s,%s)',(st_name,user[0]))
conn.commit()
var5='''
<!DOCTYPE html>
<html>
<body>
'''
print var5
if(var4[0]==0):
	print '</h> Congratulations your storage has been created!!!!</h> '
	print '<p> please click on the link below to download and execute on your pc </p>'
	print '<a href="../shell/samba.sh" download>click</a>'
else:
	print '<h> Oops your storage couldnt be created!</h>'

var6='''
</body>
</html>
'''
print var6

