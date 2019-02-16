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
     
    sql.execute('select instance_id from ec2 where user_name=%s',(user[0],))
    res=sql.fetchall()
    ec2s=[]
    for i in res:
    	ec2s.append(json.dumps(i).strip('[""]'))
     
    sql.execute('select elb_name from elb where user_name=%s',(user[0],))
    res=sql.fetchall()
    elbs=[]
    for i in res:
    	elbs.append(json.dumps(i).strip('[""]'))
     
    var1='''
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
    <form action="elb_attach_back.cgi" method="POST"> <p> Please select instances to attach to your elb </p>'''
    print var1
    for i in ec2s:
    	print '<input type="checkbox" name="ec2" value="',i,'">',i
    print '<p> your load balancers are:</p>'
    for i in elbs:
    	print '<input type="radio" name="elb" value="',i,'">',i
    var2='''
    <input type="submit">
    </form>
    </body>
    </html>
    '''
    print var2