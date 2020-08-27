from random import randint
flag = b'flag{REDACTED}'

x = randint(0,255)

ciphertext = bytearray()
for char in flag:
	ciphertext.append(char^x)

print(ciphertext.hex())