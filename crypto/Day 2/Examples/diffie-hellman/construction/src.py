from sage.all import *
from Crypto.Util.number import getPrime
from random import randint
p = getPrime(512)
F = Zmod(p)
upper_bound = F.order()
g = 2 #most likely not the prim. root so generates subgroup
a = randint(1,upper_bound-1)
b = randint(1,upper_bound-1)

B = pow(g,a,p)
A = pow(g,b,p)

shared_secret1 = pow(B,a,p)
shared_secret2 = pow(A,b,p)
assert shared_secret1 == shared_secret2
shared_secret = shared_secret1
