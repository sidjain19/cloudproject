#!/usr/bin/python2

import  cgi,cgitb,os,json,commands
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
ebs_id=web.getvalue('ebs')
ebs_id=ebs_id.strip(" ")
inst_id=web.getvalue('ins_id')
inst_id=inst_id.strip(" ")
user_name=web.getvalue('user')
user_name=user_name.strip(" ")

commands.getoutput('sudo aws ec2 attach-volume --volume-id '+ebs_id+' --instance-id '+inst_id+' --device /dev/sdf')

conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('INSERT INTO ebs_details VALUES(%s,%s,%s)',(user_name,ebs_id,inst_id))

conn.commit()
print ebs_id+'df'
sql.execute("UPDATE ebs_create SET available= %s WHERE ebs_id=%s",("NO",ebs_id)) 

conn.commit()
