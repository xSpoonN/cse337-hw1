import random as rd

def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def gcd(a,b):
    if a == 0: return b
    return gcd(b % a, a)

def lcm(a,b):
    return (a*b)/gcd(a,b)

# Generates public key exponent
def pubkExp(k):
    e = 2
    while gcd(e, k) != 1:
         e += 1
    return e

# Generate private key exponent
def prikExp(x, y):
    if (x > y):
        t = x; x = y; y = t
    for item in range(1, y):
        if (((item % y) * (x % y)) % y) == 1:
            return item
    return -1

# Returns the hash of a string message. Sum of its ascii characters.
def hash(s):
    sum = 0
    for c in s:
        sum += ord(c)
    return sum
