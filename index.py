#!C:\Python36\python.exe


print("Content-type:text/html")
print("")
print("""
<html>
    <head>
        <title>Mess Manager</title>
        <style>
            body
            {
                text-align: center;
            }

            #log
            {
                margin-top: 15%;
                height: 32%;
                width: 30%;
                background-color: aqua;
                margin-left: 34%;
            }
            #loginhead
            {
            
                
            }
        </style>
    </head>

    <body>
        <div id="log">
            
           <div id="loginhead"> <h2>LOGIN</h2>  </div>
            <br/><br/>
            <form method="POST" action="regi.py">
            Login ID: <input type="text" name="login_id" id="login_id"><br/><br/>
            Password: <input type="password" name="login_pass" id="login_pass"><br/><br/>
            <input type="submit" value="SUBMIT" name="submit" > 
            </form>
        </div><br/>
        <a href="./signup.py">Dont have an account yet? Join now!</a>
    
        <script>
            $(window).on('popstate', function(event) {
     alert("pop");
    });
        <script>


""")
import cgi, cgitb, mysql.connector
cgitb.enable()
obj=cgi.FieldStorage()
submit=obj.getvalue("submit")

role=""
if submit!=None:
    login_id=obj.getvalue("login_id")
    xpass=obj.getvalue("login_pass")
    db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
    cursor=db.cursor()
    query="select * from login where id='%s'"%login_id
    cursor.execute(query)
    result=cursor.fetchall()
    db.commit()
    resultfine=result[0]
    passw=resultfine[1]
    role=resultfine[2]
    if passw==xpass:
        print("Login successful")
        
    else:
        print("Login not successful")    
    

print('''

</body>
</html>
''')