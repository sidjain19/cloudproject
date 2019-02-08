#!/usr/bin/python2

import  cgi,cgitb,os,commands,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
usr=web.getvalue('usr')
size=web.getvalue('size')
var1=commands.getoutput(' sudo aws ec2 create-volume --size '+size+'  --region ap-south-1 --availability-zone ap-south-1a --volume-type gp2 --query VolumeId ')
var2=var1.strip('""')
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('INSERT INTO ebs_create VALUES(%s,%s,%s)',(usr,var2,"YES"))

conn.commit()
var1='''
<!DOCTYPE html>
<html>
<body>
<h1> Congratulations your ebs has been created</h1>
</body>
</html>
'''
print var1
