#!/usr/bin/python2
import  cgi,cgitb,os,commands,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
s3_name=web.getvalue('s3')
s3_name=s3_name.strip(' ')

var1=commands.getoutput('sudo aws s3 ls s3://'+s3_name)

print var1