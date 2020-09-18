from sage.all import *
from Crypto.Util.number import getPrime, bytes_to_long
pin = bytes_to_long(b'{Wonder what goes here}')

e = 3
while True:
    p = getPrime(512)
    q = getPrime(512)
    phi = (p-1)*(q-1)
    try:
        d = inverse_mod(e,phi)
        break
    except:
        pass
N = p*q
print('Can you recover my 4-digit bank PIN')
print(f'N: {N}\ne: {e}')
C = pow(pin,e,N)
print(f'C: {C}')
