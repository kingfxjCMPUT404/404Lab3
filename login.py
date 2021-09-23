#!/usr/bin/env python3
import cgi, os, secret
from templates import secret_page

#Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

if secret.username == username and secret.password == password:
    print("Set-Cookie: username = %s;" % username)
    print("Set-Cookie: password = %s;" % password)
    print("Set-Cookie: Domain = http://localhost:8080/get_data_from_form.py;")
else:
    print("Set-Cookie: username = ;")
    print("Set-Cookie: password = ;")
    print("Set-Cookie: Domain = ;")

print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<p><b>Username:</b> %s<br><b>Password:</b> %s</p>" % 
    (username, password))
print("</body>")
print("</html>")

cookie_list = os.environ["HTTP_COOKIE"].split(";")
cookies = {}
for i in cookie_list:
    if i:
        cookies[i.split("=")[0].strip()] = i.split("=")[1]

if 'username' in cookies.keys() and 'password' in cookies.keys():
    if (cookies["username"] == secret.username and
        cookies["password"] == secret.password):
        print(secret_page(secret.username, secret.password))
