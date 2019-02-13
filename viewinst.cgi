#!/usr/bin/python2

import  cgi,cgitb,os,commands,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""


user_name=web.getvalue('usr')


conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('select instance_id from ec2 where user_name=%s',(user_name,))
res=sql.fetchall()

sgrp=[]
for i in res:
	sgrp.append(json.dumps(i).strip('[""]'))
var='''


