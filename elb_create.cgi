#!/usr/bin/python2

import  cgi,cgitb,os,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()

conn=mysql.connect(user='root', password='redhat', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('select user_name from currentuser')
res=sql.fetchall()
user=[]
for i in res:
	user.append(json.dumps(i).strip('[""]'))

sql.execute('select distinct sec_grp from elb where user_name=%s',(user[0],))
res=sql.fetchall()

sgrp=[]
for i in res:
	sgrp.append(json.dumps(i).strip('[""]'))

var1='''
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("#new2").hide();
  $("#new1").click(function(){
    $("#new2").show();
    $("#exist2").hide();
  });
	
  $("#exist").click(function(){
    $("#exist2").show();
    $("#new2").hide();
  });
	
});
</script>
</head>
<body>
<form action="elb_create_back.cgi" method="POST">

<p>enter your load balancer name:</p>
<input type="text" name="elb">
<ul>
<li><input type="radio" name="radio" id="exist">select an existing security group</input></li>
<li><input type="radio" name="radio"  id="new1" >create a new security group</input></li>
</ul>
<div id="exist2">
'''
print var1
if(len(sgrp)==0):
	print '<ul><li>None</li></ul>'
else:
	for i in sgrp:
		print '<input type="radio" name="grp"  value=','"',i,'">',i
var2='''
</div >
<div id="new2">
<p>enter your security group:</p>
<input type="text" name="grp1">
</div>
<br>
<input type="submit">
</form>
<body>
</html>
'''

print var2
