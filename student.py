#!C:\Python36\python.exe
print("Content-type:text/html")
print("")

import cgi, cgitb, mysql.connector,os
import datetime

now = datetime.datetime.now()
print ("Current date: "+now.strftime("%Y-%m-%d"))
date1=now.strftime("%Y-%m-%d")
cgitb.enable()

obj=cgi.FieldStorage()
id=obj.getvalue('id')

print("""
<html>
<head>
    <title>Mess Manager</title>
</head>
<body style="text-align: center;">
<br/>
""")
if "HTTP_COOKIE" in os.environ:
    if id!=os.environ["HTTP_COOKIE"]:
        print("""   <script>window.location='http://localhost/pro1/index.py</script>  """)


else:
    print("HTTP_COOKIE not set!")
    print(""" <script>window.location='http://localhost/pro1/index.py';</script> """)
print("""
<h2>Hello """+id+"""</h2>  &nbsp;&nbsp;&nbsp;&nbsp; <a href="./index.py" onclick="delcookie()">logout</a>
<br/>
<h3>Today's Menus:</h3>
""")
db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
cursor=db.cursor()
query="select menu1 from menu where date='"+date1+"'"

cursor.execute(query)
result=cursor.fetchall()
lenz=len(result)
tupz=result[lenz-1]

db.commit()


print("Menu Contents:<br/>")
for elem in tupz:
    print(elem+"<br/>")
print("""
<form method="POST" action='regi2.py?id="""+id+"""'>

<h3>Do you like the menu?(yes/no): &nbsp;<input type="text" name="choice" id="choice"></h3><br/>
<input type="submit" style="margin-top:1%;" value="SUBMIT FEEDBACK" name="submit" id="submit"/>
</form>
<script>
function delcookie(){

    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
    
    document.location.reload()
    alert("Redirecting.........")
}
</script>
</body>
</html>

""")