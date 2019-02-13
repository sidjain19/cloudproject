#!/usr/bin/python2
import  cgi,cgitb,os,commands,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
path=web.getvalue('path')
s3_name=web.getvalue('s3')
path=path.strip(' ')
s3_name=s3_name.strip(' ')
var1=commands.getstatusoutput('sudo aws s3 cp '+path+' s3://'+s3_name)


