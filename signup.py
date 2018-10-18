#!C:\Python36\python.exe
print("Content-type:text/html")
print("")

from code import loadFile, runQuery
import cgi,cgitb,mysql.connector
cgitb.enable()
obj=cgi.FieldStorage()
submit=obj.getvalue("submit")
id=""
passw=""
role="student"

print("""

    <!DOCTYPE html>
<html>
    <head>
        <title>
            Mess Management
        </title>
    </head>
    <style>
        form {
            margin-top:40px;   
        }
        
        body {
            background-image: url('image/dinnertable.jpg');
            background-repeat: no-repeat;
            background-size: 100%;
        }

        button {
            background-color: black;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            cursor: pointer;
            width: 100%;
            border-radius:25px;
        }

        button:hover {
            opacity: 0.8;
        }

        .btn {
            width: auto;
            padding: 10px 18px;
            background-color:black;
        }

        .imgcontainer {
            text-align: center;
            margin-top:20px;
        }

        img.avatar {
            width: 10%;
            border-radius: 50%
            background-size: 50%;
        }

        .container {
            padding: 0px;
        }
    
        h1 {
            color:#C70039;
            margin-top:20px;
        }

        .C {
            border-radius: 25px;
            width:200px;
            height:20px;
            padding:9px;
        }

        .D {
            font-size: 20px;
        }   

        @media screen and (max-width: 300px) {
            span.login_pass {
                display: block;
                float: none;
            }
        }
    </style>
    
    <body>
        <form amethod="POST"><center>
            <h1 id="heading">Sign Up</h1>
            <div class="imgcontainer">
                <img src="image/signup.png" alt="Avatar" class="avatar">
            </div>
            <div class="container">
                <table cellpadding="2px">
                    <tr>
                        <td><label class="D"><b>Name</b></label></td>
                        <td><input type="text" placeholder="Enter Name" name="name" id="name" class="C" required></td>
                    </tr>
                    <tr>
                        <td><label class="D"><b>Contact Number</b></label></td>
                        <td><input type="text" placeholder="Enter Contact Number" name="contact" id="contact" class="C"></td>
                    </tr>
                    <tr>
                        <td><label class="D"><b>Email</b></label></td>
                        <td><input type="text" placeholder="Enter Email" name="email" id="email" class="C"></td>
                    </tr>
                    <tr>
                        <td><label class="D"><b>ID</b></label></td>
                        <td><input type="text" placeholder="Enter ID" name="id" id="id" class="C" required></td>
                    </tr>
                    <tr>
                        <td><label class="D"><b>Password</b></label></td>
                        <td><input type="password" placeholder="Enter Password" name="pass" id="pass" class="C" required></td>
                    </tr>
                </table>
            </div>
            <div class="container">
                <table cellspacing="20px">
                    <tr>
                        <td><button type="submit" class="btn" value="submit" name="submit">Register</td>
                    </tr>
                </table>
            </div></center>
        </form>
        
        """)

if submit!=None:
    id=obj.getvalue('id')
    passw=obj.getvalue('pass')
    name=obj.getvalue('name')
    contact=obj.getvalue('contact')
    email=obj.getvalue('email')
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
        res = runQuery(query)
        cursor.execute(query)
        db.commit()
        query = "insert into signup(name,contact,email,id,pass) values('{nm}','{cnt}','{ml}','{id}','{pd}')".format(nm=name,cnt=contact,ml=email,id=id,pd=passw)
        res = runQuery(query)
        cursor.execute(query)
        db.commit()
        print("<script>alert('Account Created. Please login on next window.'); window.location='http://localhost/pro1/index.py';</script>")
    print("""
    </body>
    </html>
    """)


