import random as rd
import mymath
from mymath.mymath import isPrime, gcd, lcm, pubkExp, prikExp, hash

class Rsa:
    # initialize to set p, q, and n.
    
    def __init__(self, p):
        prime = []
        for item in range(p, p+1000):
            if isPrime(item):
                prime.append(item)
        self.p = rd.choice(prime)
        self.q = rd.choice(prime)
        while self.p == self.q:
            self.q = rd.choice(prime)
        self.n = self.p*self.q
        
    # generates a cipher string for a message m
    def encrypt(self, m):
        k = lcm(self.p-1, self.q-1)
        e = pubkExp(k)
        # c = (m^e) % n
        c = 1; iter = 0
        while (iter < e):
            iter += 1
            c = (m * c) % self.n
        return c, e

    # decrypts a cipher string to get back original message
    def decrypt(self, c, e):
        k = lcm(self.p-1, self.q-1)
        d = prikExp(e, int(k))
        m = 1; iter = 0
        while (iter < d):
            iter += 1
            m = (c * m) % self.n
        return m
