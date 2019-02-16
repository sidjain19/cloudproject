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
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('select user_name from currentuser')
res=sql.fetchall()
user=[]
for i in res:
	user.append(json.dumps(i).strip('[""]'))

commands.getstatusoutput('sudo lvcreate --name '+st_name+' --size '+size+' share')
commands.getoutput('sudo mkfs.xfs /dev/share/'+st_name)
commands.getoutput('sudo mkdir /share_info/'+st_name)
var4=commands.getstatusoutput("sudo mount /dev/share/"+st_name+" /share_info/"+st_name)
commands.getoutput('sudo chmod 777 /share_info/'+st_name)
print var4
commands.getoutput('sudo echo /dev/share/'+st_name+' /share_info/'+st_name+'  xfs defaults 0 0 >> /etc/fstab ')
var1=commands.getstatusoutput('sudo echo /share_info/'+st_name+' 192.168.10.158\(rw\) > /etc/exports')
#commands.getstatusoutput('sudo sshpass -p redhat1 ssh root@192.168.122.106 "sudo echo /root/share_info/'+st_name+' 192.168.10.235"("rw")" > /tygh.txt"')
commands.getstatusoutput('sudo systemctl start nfs')
commands.getstatusoutput('sudo systemctl enable nfs')
commands.getoutput('sudo exportfs -r')

f=open('/var/www/html/shell/nfs.sh',mode='w')
f.write('#!/usr/bin/python2\n')
f.close()

fi=open('/var/www/html/shell/nfs.sh',mode='a')
fi.write('import commands\n')
fi.write('commands.getoutput("mkdir /mnt/'+st_name+'")\n')
fi.write('commands.getoutput("mount 192.168.10.9:/share_info/'+st_name+' /mnt/'+st_name+'")\n')
fi.close()

sql.execute('insert into nfs values(%s,%s)',(st_name,user[0]))
conn.commit()

#print var7
var5='''
<!DOCTYPE html>
<html>
<body>
'''
print var5
if(var4[0]==0):
	print '</h> Congratulations your storage has been created!!!!</h> '
	print '<p> please click on the link below to download and execute on your pc </p>'
	print '<a href="../shell/nfs.sh" download>click</a>'
else:
	print '<h> Oops your storage couldnt be created!</h>'

var6='''
</body>
</html>
'''
print var6
