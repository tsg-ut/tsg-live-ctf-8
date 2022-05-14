from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(512)
q = getPrime(512)
N = p * q
phi = (p - 1) - (q - 1)
e = 0x101
d = pow(e, -1, phi)

with open('flag.txt', 'rb') as f:
    flag = bytes_to_long(f.read())

c = []
for i in range(flag.bit_length() + 1):
    c.append(pow(flag >> i, e, N))

print(f'c = {c}')