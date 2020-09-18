from sage.all import *
from Crypto.Util.number import getPrime
from Crypto.Util.number import bytes_to_long as btl
from Crypto.Util.number import long_to_bytes as ltb
m = btl(b'flag{REDACTED}')

e = 0x10001 #65537

while True:
    p = getPrime(64)
    q = getPrime(64)
    r = getPrime(64)
    s = getPrime(64)
    phi = (p-1)*(q-1)*(r-1)*(s-1)
    N = p*q*r*s
    try:
        assert N > m
        assert gcd(e,phi) == 1 #coprime
        d = inverse_mod(e,phi) 
        break
    except:
        pass
c = pow(m,e,N)
print(f'N: {N}\ne: {e}\nC: {c}')
