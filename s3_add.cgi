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

sql.execute('select s3_name from s3 where user_name=%s',(user[0],))
result=sql.fetchall()

bucket=[]
for i in result:
	bucket.append(json.dumps(i).strip('[""]'))


var1='''
<!DOCTYPE html>
<html>
<body>
<form action="s3_add_back.cgi" method=POST>
<p>Please select your  bucket:</p>
'''
print var1
for i in bucket:
	print '<input type="radio" name="s3" value=','"',i,'">',i
var2='''
<p>Enter the complete path</p>
<input type="text" name="path">
<input type="submit">
</form>
</body>
</html>
'''
print var2
