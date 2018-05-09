#!/usr/bin/python
import os

print ("Content-type: text/html")     
print ("")

# if cookie has been set in the browser
if 'HTTP_COOKIE' in os.environ:  
    print ("""
    <html>
        <head>
            <meta charset="utf-8">
            <title>Welcome to new user</title>
            <link rel="stylesheet" type="text/css" href="index.css" />
        </head>
    <body>""")
    print("<h1>Welcome back to the site: %s</h1>") %os.environ["HTTP_COOKIE"].split("=")[0]
    print("</body>")
    print("</html>")

# otherwise present user with login screen
else:
    print ("""
    <html>
        <head>
            <meta charset="utf-8">
            <title>A2Q1</title>
            <link rel="stylesheet" type="text/css" href="index.css" />
        </head>

        <body>
            <form action="welcomeNewSignUp.cgi" method="get">
                <h1>Generic site</h1>
                <div>
                    <label for="Id">User ID:</label> 
                    <input type="text" id="id" name="user_id">
                </div>
                <div>
                    <label for="password">Password:</label> 
                    <input type="password" id="password" name="user_password">
                </div>
                <div class="button">
                    <button type="submit">Log in</button>
                </div>
            </form>
        </body>
    </html>
    """)
