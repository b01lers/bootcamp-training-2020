#Setup
from hashlib import sha256

flag = b'flag{learning_dhkey_exchange!!!}'
assert len(flag) == 32
g = 2
p = 13
a = 4
b = 5

A = pow(g,a,p)
B = pow(g,b,p)
print(f'g: {g}\np: {p}')
print(f'A: {A}')
print(f'B: {B}')
s_0 = pow(B,a,p)
s_1 = pow(A,b,p)
assert s_0 == s_1
shared_secret = s_0

hashout = bytearray.fromhex(sha256(str(a*b).encode()).hexdigest())
ctext = bytearray()
for x,y in zip(flag,hashout):
    ctext.append(x^y)
print(ctext.hex())
