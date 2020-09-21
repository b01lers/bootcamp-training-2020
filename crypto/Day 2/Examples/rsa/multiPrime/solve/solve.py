from sage.all import *
from Crypto.Util.number import long_to_bytes as ltb
N = 47283968683253223763489703863107642746052355487897544045320617987118533640129
e = 65537
C = 28528283267227040354902007252270777971329881474454910233915494489291153036353

factors = factor(N)
factors = [i[0] ** i[1] for i in factors]
phi = 1
for fac in factors:
    phi *= (fac-1)
d = inverse_mod(e,phi)
m = ltb(pow(c,d,N))
print(m)
