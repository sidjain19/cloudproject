#!/usr/bin/python2

import  cgi,cgitb,os,commands,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_name=web.getvalue('os')
sec_grp1=web.getvalue('grp1')
user_name=web.getvalue('user')
user_name=user_name.strip(' ')

cnt=web.getvalue('cnt')
commands.getoutput('sudo aws ec2 create-security-group --group-name '+sec_grp1+' --description "My security group" ')
var2=commands.getoutput('sudo aws ec2 run-instances --image-id '+os_name+' --count '+cnt+' --instance-type t2.micro --key-name "tanishanew" --security-groups '+sec_grp1+' --query Instances[0].InstanceId')
var2=var2.strip('""')
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('INSERT INTO ec2 VALUES(%s,%s,%s)',(var2,user_name,sec_grp1))

conn.commit()









