from math import gcd
exec(open('output.txt').read())

k = c[-3]

N = c[2] * k - c[1]
for i in range(3, len(c) - 3):
    if gcd(N, c[i + 1] * k - c[i]).bit_length() >= 1000:
        N = gcd(N, c[i + 1] * k - c[i])

flag = 0
for i in reversed(range(len(c) - 1)):
    flag *= 2
    flag += (c[i + 1] * k - c[i]) % N != 0

print(flag.to_bytes((flag.bit_length() + 7) // 8, byteorder='big'))
