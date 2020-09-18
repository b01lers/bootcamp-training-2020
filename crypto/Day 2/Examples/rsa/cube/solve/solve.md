So we are given that the 4-digit pin, as a string, of some bank account is encrypted using RSA

We can see in `redacted_source.py` the primes are 512 bit so factoring is going to be out the question

However if we think laterally, the largest PIN consisting of 4 digits would be "9999" and if this value is less than our modulus when we encrypt we would never take mod N of m**e

Thus, we can calculate the cube root of the ciphertext to reobtain the PIN
