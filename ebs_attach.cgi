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

sql.execute('select ebs_id from ebs_create where user_name=%s and available="YES"',(user_name,))
res=sql.fetchall()
sebs=[]
for i in res:
	sebs.append(json.dumps(i).strip('[""]'))


sql.execute('select distinct instance_id from ec2 where user_name=%s',(user_name,))
res=sql.fetchall()
sins=[]
for i in res:
	sins.append(json.dumps(i).strip('[""]'))
var='''
<!DOCTYPE html>
<html>
<body>
<form action="ebs_details.cgi" method="POST"> <p> your ebs voulmes are: </p>'''
print var
for i in sebs:
	print '<input type="radio" name="ebs" value="',i,'">',i
print '<p> your instances are:</p>'
for i in sins:
	print '<input type="radio" name="ins_id" value="',i,'">',i
print '<input type="hidden" name="user" value="',user_name,'">'
var2='''
<input type="submit">
</form>
</body>
</html>
'''
print var2

