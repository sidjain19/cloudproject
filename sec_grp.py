#!/usr/bin/python2

import  cgi,cgitb,os,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
user_name=web.getvalue('usr')

conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()

sql.execute('select distinct sec_grp from ec2 where user_name=%s',(user_name,))
res=sql.fetchall()

sgrp=[]
for i in res:
	sgrp.append(json.dumps(i).strip('[""]'))

var='''
<!DOCTYPE html>
<html>
<body>
<form action="ec2py.cgi" method="POST">

<p><b>Instance :
<br>
<input type="radio" name="os" value="ami-5b673c34" checked>Redhat<br>
<input type="radio" name="os" value="ami-0d773a3b7bb2bb1c1"> Ubuntu<br>
<input type="radio" name="os" value="ami-0209d238252cbc9fe">Windows<br>
</p>

<p><b>security group :
(Please copy your security group and paste in the text field below)
Your Existing Security groups are : 
<ul>'''



print var
for i in sgrp:
	print '<li>'+i+'</li>'




var1='''
</ul>
<input type="text" name="grp1">
<br>
Create a new security group : <br>
<input type="text" name="grp1"><br>
</p>

<p><b>Number of Instances :
<input type="number" name="cnt"><br>
</p>
<input type="hidden" id="custId" name="user" value='''
print var1,'"',user_name,'"'
var2='''>

<input type="submit">
</form>
<body>
</html>'''

print var2



