import numpy as np
from flag import flag

class RNG:
    def __init__(self):
        self.p = np.random.randint(2**32)
        self.q = np.random.randint(2**32)
        self.r = np.random.randint(2**32)
        self.x = np.random.randint(2**32)
    def next(self):
        self.x = (self.p * self.x + self.q) % self.r
        return self.x

money = 5
rng = RNG()
print("GAME OF ROULETTE")
print("Obtain 1 million money to earn a secret flag!")
for round in range(7):
    print("--------------------")
    print("Round {}".format(round+1))
    print("You have {} money.".format(money))
    a = int(input("How much will you bet?\n> "))
    assert 1 <= a <= money
    n = int(input("What number will you bet on?\n> "))
    assert 0 <= n <= 36
    m = rng.next() % 37
    print("Your guess: {} Result: {}".format(n, m))
    if n == m:
        print("You win {} money!".format(a*36))
        money += a*36
    else:
        print("You lose {} money.".format(a))
        money -= a
    if money <= 0:
        print("You are broke.")
        break
    if money >= 1000000:
        print("Good job! Here is your flag: {}".format(flag))
        break
print("GAME OVER")
