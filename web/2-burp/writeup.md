# Burp Challenge
- This example walks you through some basic Burp functionality.

## Step 1
- The first step is outlined on the index page. Set up and turn the proxy on, then type in any username and password.
- The request should pop up in the intercept window and you can see what's being sent to the server.
- Here is an example request:
```
POST / HTTP/1.1
Host: localhost:5002
Content-Length: 28
Connection: close

username=admin1&password=admin_password
```

- You can see your username and password being sent at the bottom in the form `username=inputted_username&password=inputted_password`
- Sending the request to the repeater it will make it easier to continually make incremental changes and watch the response.
- There's a new header that pops up:
```
Try This In Your Browser For It To Work: Username: 'Rick' & Password = 'hunter2'
```

- If you try it in your browser you get redirected to 'Rick Astley Never Gonna Give You Up'
    - AKA you got Rick Rolled.
- This is a nice example of a couple things:
    1. CTF makers are big memers
    2. We also create things called 'red herrings'. These are fake hints to the solution to keep players on their toes.

## Step 2
- If you intercept the request after typing in the username and password, you get this page:
```html
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 631
Server: Werkzeug/1.0.0 Python/3.7.8
Date: Sat, 08 Aug 2020 03:13:10 GMT


<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Burp Example</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link
      rel="stylesheet"
      href="/static/css/bootstrap.min.css"
    />
    <script>
      window.location.assign("https://www.youtube.com/watch?v=dQw4w9WgXcQ");    <--- Rick roll redirect here
    </script>
  </head>

  <body>
    <div class="jumbotron text-center">
      <h1 class="display-1">Burp Example</h1>
    </div>
    <div class="content">
      <div>
        <p>%62%30%63%74%66%7b%62%75%72%70%5f%72%6f%63%6b%73%21%7d</p>           <--- This is interesting
      </div>
    </div>
  </body>
</html>
```
- That looks like a url encoded string.

### Decoder
- We can copy that string to the Decoder, or select it, right click & send to decoder
- Decode as url to get the flag: `b0ctf{burp_rocks!}`
