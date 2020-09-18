from Crypto.Util.number import getPrime, inverse
from Crypto.Util.number import bytes_to_long as btl
from Crypto.Util.number import bytes_to_long as ltb

m_1 = btl(b'REDACTED')
moduli = []
for _ in range(3):
    p = getPrime(128)
    q = getPrime(128)
    N = p*q
    moduli.append(N)

e = 3

for n in moduli:
    assert pow(m_1,e) > n
    
ciphertexts = []
for n in moduli:
    ciphertexts.append(pow(m_1,3,n))
    
print(ciphertexts)
print(moduli)
