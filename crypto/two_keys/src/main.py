from Crypto.Util.number import *
from flag import flag

def nextPrime(n):
    while True:
        n += 1
        if isPrime(n):
            return n

class RSA:
    def __init__(self, p, q):
        assert isPrime(p) and isPrime(q)
        self.p = p
        self.q = q
        self.e = 65537
        self.d = pow(self.e, -1, (self.p-1) * (self.q-1))
    def encrypt(self, x):
        return pow(x, self.e, self.p * self.q)
    def decrypt(self, y):
        return pow(y, self.d, self.p * self.q)
    def printPublicKey(self):
        print(f"N = {self.p * self.q}")
        print(f"e = {self.e}")

p = getPrime(512)
q = getPrime(512)
pp = nextPrime(p)
qq = nextPrime(q)
rsa1 = RSA(p, q)
rsa2 = RSA(pp, qq)

x1 = int.from_bytes(str.encode(flag[:len(flag)//2]), "big")
x2 = int.from_bytes(str.encode(flag[len(flag)//2:]), "big")
y1 = rsa1.encrypt(x1)
y2 = rsa2.encrypt(x2)

assert x1 == rsa1.decrypt(y1)
assert x2 == rsa2.decrypt(y2)

print("First half:")
rsa1.printPublicKey()
print(f"y = {y1}")
print()
print("Second half:")
rsa2.printPublicKey()
print(f"y = {y2}")
