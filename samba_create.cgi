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

sql.execute('select storage_name from smb where user_name=%s',(user[0],))
result=sql.fetchall()

nfs=[]
for i in result:
	nfs.append(json.dumps(i).strip('[""]'))

var1='''
<!DOCTYPE html>
<html>
<body>
<p><b>your existing object storages are:</p>
'''
print var1
if(len(nfs)==0):
	print '<ul><li>None</li></ul>'
	print '<br><br>'
else:
	print '<ul>'
	for i in nfs:
		print '<li>',i,'</li>'
	print'</ul>'
var2='''
<form action="samba_create_back.cgi" method=POST>
<p>enter storage name:</p>
<input type="text" name="storage" placeholder="storage name">
<p>enter the size for your storage:</p>
<input type="text" name="size" placeholder="size in Mib">
<p>Enter your ip address:</p>
<input type="text" name="ip" placeholder="ipv4 address">
<input type="submit">
</form>
</body>
</html>
'''
print var2
