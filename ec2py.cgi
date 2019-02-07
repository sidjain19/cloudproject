#!/usr/bin/python2

import  cgi,cgitb,os,commands,time,subprocess,qrcode,json
cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_name=web.getvalue('os')
sec_grp=web.getvalue('grp')
cnt=web.getvalue('cnt')
var1=commands.getoutput('sudo aws ec2 create-security-group --group-name '+sec_grp+' --description "My security group" --query "GroupId" ')
#print var1
var2=commands.getoutput('sudo aws ec2 run-instances --image-id '+os_name+' --count '+ cnt+' --instance-type t2.micro --key-name "tanishanew" --security-group-ids '+var1+' --subnet-id subnet-0352eb4f')
print var2

