    #!/usr/bin/python2
     
    import  cgi,cgitb,os,json
    import mysql.connector as mysql
     
    cgitb.enable()
     
    print  "Content-type:text/html"
    print  ""
     
    web=cgi.FieldStorage()
    inst_id=web.getvalue('ec2')
    elb=web.getvalue('elb')
     
    elb=elb.strip(' ')
    for i in range(len(inst_id)):
    	inst_id[i]=inst_id[i].strip(' ')
     
    for i in inst_id:
    	commands.getoutput('sudo aws elb register-instances-with-load-balancer --load-balancer-name '+elb+' --instances '+i)
     
    var1='''
    <!DOCTYPE html>
    <html>
    <head>
    <h2>Congratulations!! Your Instances are attached with the ELB!!<h2>
    </html>
    '''
    print var1