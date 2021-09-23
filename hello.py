#!/usr/bin/env python3
import os, json

print("Content-type: text/html\r\n\r\n")
print
print("<title>Test CGI</title>")
print("<p>Helo World</p>")


# Q1
print("<br>\n------------<br>\nQ1<br>\n------------<br>\n")
print(os.environ, "<br>")

print("<br>json:<br>")
json_object = json.dumps(dict(os.environ), indent=4)
print(json_object)

# Q2
print("<br>\n------------<br>\nQ2<br>\n------------<br>\n")
for param in os.environ.keys():
    if param == "QUERY_STRING":
        print(f"<em>{param}</em> = {os.environ[param]}</li>")
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

# Q3
print("<br>\n------------<br>\nQ3<br>\n------------\n<br>\n")
for param in os.environ.keys():
    if param == "HTTP_USER_AGENT":
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
