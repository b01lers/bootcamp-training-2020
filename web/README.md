# Web lessons for the 2020 bootcamp

## Day 1
### Quick intro
- Welcome to the first training session for the 2020 bootcamp! This first week we have two sessions on the basics of web.
- Web is a cool but vast topic.
- I like web because I use websites every day and knowing how they work is interesting to me.
- New tech is coming out all the time for web, js frameworks, web assembly, etc.
- New code means new vulnerabilites which is always exciting for security researchers and ctf developers.
- When ctf challenges have new tech it encourages participants to learn and together the relationship of ctf developers and players
    grow the security community.


### Engagement
- What devices have web components?
    - Routers
    - Computers
    - CUPS (printing on linux)
    - Your personal computer? Web browser.
    - ELECTRON??
- What web hacking terms have you heard of?
    - XSS Cross Site Scripting
    - Template Injection
    - SQL injection
    - Misconfigurations
        - Open s2 boxes
    - Insecure deserialization
- How many of you have already mastered web skills / have never heard of HTML in their life / somewhere in the middle
    - No one is a master --> tech is constantly evolving.
- If you have a question or something doesn't make sense please type in the chat and one of the b01lers officers 
    will help you and I'll be checking in to see if I can help clarify anything as well.


### Interactive Demo 0
- So instead of lecturing for a couple hours, I've prepared some demos to go over.
- They are in your docker container already **TODO where??**
- This demo is intended to show how useful the developer tools in your browser are.
- Before you begin I have to assume you all know nothing about how a website works so stick with me while I cover some basics.
- This is how you view webpages.

#### Opening browser dev tools
- Open the dev tools by right clicking and selecting 'inspect element'
- F-12 is a pretty universal hotkey for most browsers.

#### Inspect element
- Inspect element / inspector is a great tool to see the html of the site. It organizes html elements by tag and you can expand and collapse
    tags until you find what you're looking for. A useful feature is if you scroll over a tag it might highlight on the screen if it is
    visible.

#### Console
- This is a javascript console, it is super powerful. This window can call functions in \<script\> tags and is a nice place 
    to run javascript snippets that interact with the current web page.

#### Debugger
- This is a javascript debugger, it is also very powerful. You can set breakpoints and change values. This is how my high score
    for that facebook messenger basketball game is over 10.

#### Network
- This is where you can see all the requests your browser sends to the server and the responses it receives back from the server.
- Quick demo:
1. You type into your browser www.google.com
    - See all the requests your browser makes just by going to one website.
    - We can filter the requests by clicking the html button above the list of results. **Chrome doesn't have an option to filter
        by html??**
2. Your browser sends a message, in a very specific form, called a GET request to www.google.com that asks for the index (base / root / starting point of the website, much like the root of the linux filesystem '/')
    - You can think of this as the language that browsers and webservers use to communicate with each other.
    - Every request is in a specific form, we can view the request by clicking on any of the entries and clicking 'headers' on the new window that appears.
    - Then scroll down to the 'Request headers' entry and select the 'raw' toggle in firefox.
    - Most requests contain only this headers section, but they can contain a body.
3. Google's server receives your request and sends back a response. This response has 2 parts: the headers and the body.
    - The headers are information useful for the browser such as status codes (404 not found, 302 redirect, etc..)
    - The body of a response is the webpage data (html, css, js, or more). This is the content of the page and what you usually see when browsing the internet.
    - Most responses have a body, but responses don't have to have one. Ex: HEAD only returns response headers.

#### Storage
- You can view the cookies that the domain is storing in your browser. You can edit the values here as well.


- This first demo has 4 flags to find.
**Do I say this or nah?**
- You may also notice that you have source and a writeup. These are practice challenges and are meant to help you get in the mindset of
    problem solving. Yes looking at the source & writeup might be the easiest and you'll be the first one to solve the challenge,
    but then you'll be sitting there for 10 minutes without anything to do. I will go over the solutions at the end so everyone can understand
    how to solve each part.
- To start it go into type `./web/0-basic_dev_tools.sh`
- This will start the web server for the basic dev_tools example and store the logs in `~/web/logs/0-basic_dev_tools.log`


### Interactive Demo 1
- This demo is all about different HTTP methods. By browsing the web you tend to only use GET and POST, but there are more defined.
- This demo walks you through the other methods and how to send them.
- There are 2 flags with this demo and there is a part 2. Once you get the flag from part 1 you should use that as a hint to finding part 2.


### Quick burp demo
- [https://github.com/opsxcq/docker-vulnerable-dvwa](https://github.com/opsxcq/docker-vulnerable-dvwa)
- dvwa `docker run --rm -it -p 80:80 vulnerables/web-dvwa`
- localhost/setup.php
- pass: `admin` `password`
- Brute force
- You'll be able to try to brute force into a website Friday


### Interactive Demo 2
- To start off we need to install the burp certificate so our browser doesn't throw a security error when we try to intercept our traffic.
- [Install burp certificates](https://support.portswigger.net/customer/portal/articles/1783075-installing-burp-s-ca-certificate-in-your-browser)
- [Set up proxy switcher for firefox with foxyproxy](https://howtotechglitz.com/using-burp-foxyproxy-to-easily-switch-between-proxy-settings-null-bytes-wonderhowto/)

#### Part 1 what is the proxy
- This tab hanndles all of the intercepted traffic, you get to view your request before you send it and can change it however you like.
- This is nice because it gives you a quick look into what the request is and if there is anything being sent from the website that is hidden.
- **Note** This can get crowded if you've got a lot of windows open, so make sure to open a fresh window or close your tabs.
- **Note** You can also forget that you have this on and so when you go to visit a page it will appear as if you can't connect to it because the request is stuck in burp.
- **Note** Please don't spider the challs it just follows links and crawls a website, but it generates a ton of traffic
- Editing a request

#### Part 2 what is the repeater
- This tab allows you to repeatedly change one request as many times as you'd like and see if the response changes.

#### Part 3 intruder
- This tab allows you to send predifined values over and over again. You can use this to brute force a login.
- Load in password list (only use 500 worst passwords for this)


### Interactive Demo 3
- This is a demo about SQL. My reccommendation to all of you is to teach yourself more about databases by taking a databases course or building a project with a database to see how people use databases and how to build one yourself.
- This might be hard for some of you to follow along with but we're here to help so ask questions if you're stuck!
- 2 Flags

### XSS game
- [https://xss-game.appspot.com/](https://xss-game.appspot.com/)
