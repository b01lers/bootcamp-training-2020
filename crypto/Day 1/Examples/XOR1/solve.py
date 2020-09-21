ciphertext = bytearray.fromhex('69636e68747c3e61683e6a506d767b3c50773f7d72')

# Brute force
def brute_force():
	for x in range(256):
		output = bytearray()
		for char in ciphertext:
			output.append(char^x)
		if b'flag' in output:
			print(output.decode())

def known_plaintext():
	# Known-plaintext 
	first_byte = ciphertext[0]
	known = ord('f') #from flag format

	pad_byte = first_byte ^ known

	message = bytearray()
	for char in ciphertext:
		message.append(pad_byte^char)
	print(message.decode())

brute_force()