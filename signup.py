#!C:\Python36\python.exe
print("Content-type:text/html")
print("")
print("""
<html>
<head>
<title>Mess Management</title>
</head>

<center><h1>Sign Up</h1></center>
<center><form method='POST' >
Create ID: &nbsp;
<input type='text' name='id' id='id'><br/><br/>
Create Password: &nbsp;
<input type='password' name='passw' id='passw'><br/>
<br/>
<input type="submit" value="submit" onclick="msg()" name="s">
</form>
</center>

""")

import cgi,cgitb,mysql.connector
cgitb.enable()
obj=cgi.FieldStorage()
submit=obj.getvalue("s")
id=""
passw=""
role="student"

if submit!=None:
    id=obj.getvalue('id')
    passw=obj.getvalue('passw')
    db=mysql.connector.connect(host='localhost',user='root',password='',database='mess')
    cursor=db.cursor()
    query="select id from login where id='"+id+"'"
    cursor.execute(query)
    result=cursor.fetchall()
    
    db.commit()
    if len(result)>0:
        print("<script>alert('Username is already taken. Choose another one.')</script>")
        print("")
    else:
        cursor=db.cursor()
        query="insert into login values('"+id+"','"+passw+"','student')"
        cursor.execute(query)
        db.commit()
        print("<script>alert('Account Created. Please login on next window.'); window.location='http://localhost/pro1/index.py';</script>")
    print("""
    
    </body>
    </html>

    """)


