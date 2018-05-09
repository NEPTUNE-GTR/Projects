#!/usr/bin/python
import os

qs = os.environ['QUERY_STRING']

qsParams = {}
splitString = [s for s in  os.environ['QUERY_STRING'].split('&') if s]
for item in splitString:
    name, password = item.split('=')
    qsParams[name] = password



if qsParams['user_id'] == "marker" and qsParams['user_password'] == "marker":
    print ("Set-Cookie:" +  str(qsParams['user_id']) + "=" + str(qsParams['user_password']))

print ("Content-type: text/html")
print ("")

print ("""
<html>
    <head>
        <meta charset="utf-8">
        <title>Welcome to new user</title>
        <link rel="stylesheet" type="text/css" href="index.css" />
    </head>

    <body>""")
if qsParams['user_id'] == "marker" and qsParams['user_password'] == "marker":
    print("<h1>Welcome to the site: %s</h1>") %qsParams['user_id']

else:
    print("<p>Error, not a registred member</p>")

print("</body>")
print("</html>")
