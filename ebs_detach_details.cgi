#!/usr/bin/python2

import  cgi,cgitb,os,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('select user_name from currentuser')
res=sql.fetchall()
user=[]
for i in res:
	user.append(json.dumps(i).strip('[""]'))
#print user[0]
sql.execute('select ebs_id from ebs_create where user_name=%s and available="NO"',(user[0],))
res=sql.fetchall()
att=[]
for i in res:
	att.append(json.dumps(i).strip('[""]'))
var1='''
<!DOCTYPE html>
<html>
<body>
<form action="ebs_detach.cgi" method=POST>
<p>The id's of the attached ebs are:</p><br>'''
print var1
for i in att:
	print '<input type="radio" name="ebs_id" value=','"',i,'">',i
var2='''
<input type="submit" placeholder="detach"> 
</form>
</body>
</html>
'''
print var2
