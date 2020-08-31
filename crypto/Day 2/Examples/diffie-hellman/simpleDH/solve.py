from hashlib import sha256
g = 2
p = 13
A = 3
B = 6
ctext = bytearray.fromhex('93a6599033cdb38b8548d1ca48ea11abac7a613bcd6c50691943865883f80156')

#Much better algorithms 
#https://www.alpertron.com.ar/DILOG.HTM
#BSGS and Pohlig-Hellman
def brute_dlog(base,result,modulus):
    for i in range(modulus-1):
        if pow(base,i,modulus) == result:
            return i
a = brute_dlog(g,A,p)
b = brute_dlog(g,B,p)

hashKey = str(a*b).encode()
pad = bytearray.fromhex(sha256(hashKey).hexdigest())
for x,y in zip(pad,ctext):
    print(chr(x^y),end='')
