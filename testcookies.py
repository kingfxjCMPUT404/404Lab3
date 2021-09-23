#!/usr/bin/env python3
import os

print("Set-Cookie: UserID = XYZ;")
print("Set-Cookie: Password = XYZ123;")
print("Set-Cookie:xpires: = Tuesday, 31-Dec-2007 23:12:40 GMT;")
print("Set-Cookie: Domain = www.tutorialspoint.com;")
print("Content-Type: text/html\r\n\r\n")
print('<html>')
print("<head>")
print("<title>COOKIED SET - First CGI Program</title>")
print("</head>")
print("<body>")
print(("<h2>All Done!</h2>"))
print("<body>")
print("</html>")

for param in os.environ.keys():
    if param == "HTTP_COOKIE":
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
