#!/usr/bin/python2

import  cgi,cgitb,os,commands,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
ebs_id=web.getvalue('ebs_id')
ebs_id=ebs_id.strip(" ")
commands.getoutput('sudo aws ec2 detach-volume --volume-id '+ebs_id)
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('DELETE from ebs_details where ebs_id=%s',(ebs_id,))
sql.execute('UPDATE ebs_create SET available="YES" where ebs_id=%s',(ebs_id,))
conn.commit()
var1='''
<!DOCTYPE html>
<html>
<body>
<h1> Your EBS is detached!!!</h1>
</body>
</html>
'''
print var1
