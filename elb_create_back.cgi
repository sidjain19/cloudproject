#!/usr/bin/python2

import  cgi,cgitb,os,json,commands
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
elb=web.getvalue('elb')
sec_grp=web.getvalue('grp1')
exist_grp=web.getvalue('grp')
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('select user_name from currentuser')
res=sql.fetchall()
user=[]
for i in res:
	user.append(json.dumps(i).strip('[""]')
if(sec_grp==None):
	
sg_id=commands.getoutput('sudo aws ec2 create-security-group --group-name '+sec_grp+' --description "My security group" --query GroupId ')
commands.getoutput('sudo aws ec2 authorize-security-group-ingress --group-name '+sec_grp+' --protocol tcp --port 80  --cidr 0.0.0.0/0')
var1=commands.getoutput('sudo aws elb create-load-balancer --load-balancer-name '+elb+' --listeners "Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80" --security-groups '+sg_id+' --availability-zones ap-south-1a --query DNSName')

print "Your DNS for ELB is: "+var1

sql.execute('INSERT INTO elb VALUES(%s,%s,%s)',(elb,user[0],sec_grp))
conn.commit()

