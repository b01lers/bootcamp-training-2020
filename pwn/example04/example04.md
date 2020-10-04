# PWN Example 04

This example will explain the Global Offset Table - GOT, and how it can be used in some cases to bypass PIE protections.

It will also introduce libc, and show how library functions that are loaded every time a binary is run can be used to gain code execution.

## Libc

When programs use functions such as `printf`, `system`, or `fgets`, the code must be stored somewhere. The location that this code is stored is called a `library`. Some programs have their own libraries, but the most common functions are provided by `libc`.

If you open up a library in your favorite disassembler, it would look much like a normal binary, it might just have slightly different sections, and no `main`.

When we run our program, we can see that libc is loaded, and that it is in contiguous memory by printing the addresses of functions in libc.
```
Try these in GDB:
p printf
p system
info process maps
```

This means that even functions that are never called by your program will still be loaded in memory for your program, if they are in the library.

### A Note about ASLR

ASLR will cause libc to be loaded into a different place each run. This means that to return to a libc address, you will need a leak of some sort. Once you have one libc leak, you will be able to calculate any other libc address.

### Win Function 2.0

Up until now, most of the examples had some sort of a `win` function that you would jump to and get a shell. It turns out that even some of the hardest challenges still work similarly - all you have to do is call a function, and sometimes set up arguments. In our case, the 'win functions' will just be be loaded by libc.

One of the most commonly used functions for that is `system`. The only argument required is the string "/bin/sh" or whatever command you wish to execute.

In addition, there are what are called `one_gadgets`. These are small sections of code in libc that, given a few constraints, will get a shell on their own. The `one_gadget` tool (installable through `pip install one-gadget` or via a ruby gem) will search a libc for gadgets and show their constraints.

```
━━┫ one_gadget /usr/lib/x86_64-linux-gnu/libc-2.31.so 
0xe6ce3 execve("/bin/sh", r10, r12)
constraints:
  [r10] == NULL || r10 == NULL
  [r12] == NULL || r12 == NULL

0xe6ce6 execve("/bin/sh", r10, rdx)
constraints:
  [r10] == NULL || r10 == NULL
  [rdx] == NULL || rdx == NULL

0xe6ce9 execve("/bin/sh", rsi, rdx)
constraints:
  [rsi] == NULL || rsi == NULL
  [rdx] == NULL || rdx == NULL
```

## Global Offset Table

The Global Offset Table or GOT will be loaded with the addresses of libc (and other library) functions. Every time a library function is called, the address of the function will be looked up in the GOT table, and that address will be called. If a way to leak a value in it can be discovered, you can calculate any libc address. If a way to write to it can be discovered, you can make it so that when a library function is executed, an address you choose is executed instead.

## Example

Take a quick look to see if you can identify the vulnerability before you start this example.
```c
#include <stdio.h>
#include <stdlib.h>

long numbers[16];

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char inp[16];
    int c;

    while(1) {
        printf("Which number would you like to write to?\n> ");
        fgets(inp, 16, stdin);
        c = atol(inp);
        printf("What value should be written?\n> ");
        fgets(inp, 16, stdin);
        numbers[c] = atol(inp);
        printf("Which number would you like to print?\n> ");
        fgets(inp, 16, stdin);
        c = atol(inp);
        printf("%lu\n", numbers[c]);
    }

}
```

The bug here is the same as in example01: An unbounded index. In this challenge, the index is for an item in the BSS, but PIE is enabled, so we are unable to use that to access the stack or heap. The GOT segment is adjacent to the BSS, however, so we can use this to read and write from the GOT table.

A good target GOT entry in this challenge is strtol. This is partly because it is called with a controlable input, and at a good location in the program. Identifying the best entries in the GOT table can sometimes be a puzzle, depending on the layout of the program.

Since we will need to know this offset, we can do math on the addresses in Ghidra, or we can use pwntools again, which can calculate the offset based on the available symbols. Sometimes it is not clear which symbols to use, so you can list all symbols in an interactive pwntools prompt with:
```python
>>> binary.symbols
{
 "symbol1": 1234,
 "symbol2": address,
 ...
}
```

This is sometimes useful, since different tools will use a different notation for symbols representing elements in the GOT.

We can find the offset in bytes by subtracting the addresses - the offset will be the same even if PIE is enabled. We will need to divide by 8 to find the offset in longs, which is what our index is.
```python
strtol_got = binary.symbols['got.strtol']
numbers = binary.symbols['numbers']
offset = (strtol_got - numbers) / 8
```

Once we have the offset, we can leak the address of strtol, a libc function.

The rest of this explanation is incomplete. You can watch the lesson on youtube for more details.

The final step will be to calculate the address of system based on the address of `strtol`, then overwrite the atoi entry in the GOT table with the address of system `system`
