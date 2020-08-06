# HTTP methods
- The first page you pull up gives you a flag and a nice description of the different methods.

## GET
- Just using a browser to view the page will give you part 1 of the flag: `b0ctf{`

## HEAD
```
$ curl -I [website]
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 0
flag-part2: part2_
...snip...
```

## POST
```
$ curl -X POST [website] -d arg1=doot
<h2 id="flag">Flag pt 3 of 6: 'is_GET'</h2>
```

## PUT
```
$ curl -X PUT [website] -d arg1=doot
<h2 id="flag">Flag pt 4 of 6: 'ting_r'</h2>
```

## DELETE
```
$ curl -X DELETE [website]
<h2 id="flag">Flag pt 5 of 6: 'obots.'</h2>
```

## OPTIONS
```
$ curl -X OPTIONS [website]
Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS
flag part 6: 'txt}'
```


- Putting everything together
1. b0ctf{
2. part2_
3. is_GET
4. ting_r
5. obots.
6. txt}
- b0ctf{part2_is_GETting_robots.txt}

## Part 2
- Using the flag from part 1 we can see that we have to GET robots.txt
- To do this you can just type in [url]/robots.txt
```
#=-------------------------------------------=#
# README
# Robots.txt is a text file that
# define boundaries for web scrapers.
# A web scraper is a bot someone makes
# to follow all links on web pages to
# build a map or to archive content.
# They should read the robots.txt file
# before following the link so they
# don't flood the server with requests
# from non users.
# Flag: b0ctf{congrats_welcome_to_the_botnet}
#=-------------------------------------------=#

User-agent: *
Disallow: /

# No search result pages
Disallow: /*?

# Chrome new tab page
Disallow: /chrome_newtab

User-agent: ia_archiver
Disallow: /

```
