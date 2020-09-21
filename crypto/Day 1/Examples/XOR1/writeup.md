# XOR 1 Demo Challenge

Basic example showing how we can attack a single byte xor in two ways
	- Using the flag format to determine the pad character
	- Can easily enumerate all 256 possibilities

# Solution
1. Using the flag format
In the case of this attack, we know that the flag format holds and that the "one-time pad" is only using a single byte rather than a string of bytes equal to the length of the message.
Attack:
- Flag format is: `flag{.*}`
- ord('f')^ciphertext[0] = pad_character
- Can use the pad character to decrypt from there because each character in the flag is xor'd with it
	- If c = a^b, then c ^ b = a ^ b ^ b = a. Since x ^ x = 0 and x ^ 0 = x. 