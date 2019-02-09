#!/usr/bin/python2
import  cgi,cgitb,os,commands,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
user_name=web.getvalue('usr')
s3_name=web.getvalue('s3')
s3_name=s3_name.strip(' ')
var1=commands.getstatusoutput('sudo aws s3 mb s3://'+s3_name)
conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
if var1[0]==0:
	sql.execute('INSERT INTO s3 values(%s,%s)',(s3_name,user_name))
        conn.commit()
var2='''
<!DOCTYPE html>
<html>
<body>
'''
print var2
if var1[0]==0:
	print '<h1>Congratulations your bucket has been created !!!</h1>'
        
else:
	print '<h1>Oops your bucket could not be created because it was not dns-complient</h1>'
	print '<p> please click on the link below to try again</p>'
        print '<a href="../s3_create.html">click</a>'
var3='''
	


</body>
</html>
'''
print var3
