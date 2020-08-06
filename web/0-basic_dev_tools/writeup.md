# Basic Devtools Example
- Start by pressing `f12` or right click -> inspect element to open up the inspect element tools

## Flag 1 Inspect element (column 1)
- When you first open up the window you should see a bunch of tabs, click the one on the left that says 'Inspector'.
- This lets you see the html page that the server sends you. Note the fact that I said "The server sends you" this will come up later.
- Anyway we have two panes that have opened up now, the left one and the right one.
- The left one shows the current html file you are viewing in your browser while the right one shows style information (at least in firefox).
- If you scroll your mouse over each element in the left frame, you can see that the corresponding element in the browser gets highlighted.
- You can click the arrow beside each tag to expand it, and click it again to re hide it.
- The first flag is in a comment directly under the jumbotron div that displays the Basic Devtools Example title.
```
<!-- Part 1: Look at the comments, they're helpful! first flag: b0ctf{web_example_1!}-->
```

- You can think of inspect element as a debugger for a website.
- An alternative to inspect element is 'view source' this is useful for viewing all of the html without having to expand each \<div\> tag, but you don't get the highlighting.

## CSS (column 2)
### Flag 2: Part 1
- Continuing on to the next challenge, CSS.
- For this challenge stay on the inspector tab and find the column 2 div. To do this you can look through each of the divs until you find the div with the column 2 id. This will look like: `<div id="column 2" class="col-sm-4">`
- This might seem super easy (the flag is just in the html, what's the point) but the challenge here is not getting the flag, but showing you that you can change the html in your browser through the inspector.
- Right click the div -> edit as HTML, or just double click it and remove the background color and you've uncovered the flag.

### Flag 3: Part 2 (This one is kinda harder)
- At first it appears that there isn't anything there, but when you look at the html you will find a div with 0 opacity. Change the opacity to > 0 and you'll be able to see the 'Click me!' button.
- Except when you click it, it doesn't do anything...
- Looking at it closer you can see it has `disabled="False"`.
- Changing the value from False to True doesn't do anything, but that would mean it would be disabled?
- Just delete it.
- Once you've remomved the `disabled="False"` from the tag you can click the button and it'll take you to flag2.5.html
```
b0ctf{was_it_harder?}
```
- Additional challenge, where else can you find flag2.5.html from the main page?

## Flag 4 Javascript
- At the bottom of this column there's a login section.
- Just tring a random username and password gets us nothing, but if you still have inspector open, go ahead and find the column 3 div.
- Look for the \<script\> tag, this tag means that it contains javascript code. The following is an excerpt from the challenge.
```
<script>
  function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    if(username === "admin" && password === "passw0rD") window.location='flag3.html';
    else document.getElementById("alert").style.display = 'block';
  }
  ...
</script>
```
- Looking at the `username` and `password` variables, they are being assigned to the username and password values.
- The two lines with `let ... = ...` store the username and password input you type into the variables `username` and `password`.
- The next line compares each of those variables to the values "admin" and "passw0rD".
- Using the power of deductive reasoning, let's try typing "admin" into the username box and "passw0rD" into the password box.
- And `_rt_niisis_idebecs}eten0ujl{_cscf` doesn't look like a flag.
- There's another \<script\> tag with this Javascript.
```
<script>
  function unscramble() {
    let scrambled = document.getElementById("flag").innerText;
    let unscrambled = scrambled.split('');
    unscrambled[0] = scrambled[14];
    unscrambled[1] = scrambled[23];
    unscrambled[2] = scrambled[16];
    unscrambled[3] = scrambled[20];
    unscrambled[4] = scrambled[32];
    unscrambled[5] = scrambled[27];
    unscrambled[6] = scrambled[29];
    unscrambled[7] = scrambled[26];
    unscrambled[8] = scrambled[5];
    unscrambled[9] = scrambled[13];
    unscrambled[10] = scrambled[4];
    unscrambled[11] = scrambled[2];
    unscrambled[12] = scrambled[0];
    unscrambled[13] = scrambled[7];
    unscrambled[14] = scrambled[6];
    unscrambled[15] = scrambled[12];
    unscrambled[16] = scrambled[15];
    unscrambled[17] = scrambled[3];
    unscrambled[18] = scrambled[25];
    unscrambled[19] = scrambled[30];
    unscrambled[20] = scrambled[10];
    unscrambled[21] = scrambled[8];
    unscrambled[22] = scrambled[9];
    unscrambled[23] = scrambled[28];
    unscrambled[24] = scrambled[11];
    unscrambled[25] = scrambled[22];
    unscrambled[26] = scrambled[17];
    unscrambled[27] = scrambled[19];
    unscrambled[28] = scrambled[16];
    unscrambled[29] = scrambled[24];
    unscrambled[30] = scrambled[1];
    unscrambled[31] = scrambled[21];
    unscrambled[32] = scrambled[18];
    console.log(unscrambled.join(''));
  }
</script>
```
- I assume this unscrambles the flag, but there isn't any way in the html to call the function.
- We can create our own button to call the function, but that's too much work, switch to the console tab in the inspect element tool.
- From here we have a Javascript interpreter where we can run Javascript in.
- You can try out some Javascript syntax, or call the unscramble function like so:
```javascript
>> unscramble()
b0ctf{client_side_js_is_insecure}
```

