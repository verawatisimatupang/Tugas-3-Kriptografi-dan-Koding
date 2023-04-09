# Menu pembangkitan kunci publik dan kunci privat RSA
# 1: pilih dua bilangan prima sembarang, p dan q
import random
# maxLength = 1000000000000

def isPrime(number):
    if(number < 2):
        return False
    else:
        for i in range(2, number):
            if((number % i)) == 0:
                return False
        return True

# ini masih bilangan yang ga besar
def primeNumber(minRange, maxRange):
    while(1):
        number = random.randint(minRange, maxRange)
        if isPrime(number):
            return number

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def eValue(totient):
    while(1):
        e = random.randint(1, totient)
        if(gcd(e, totient)==1):
            break
    return e

def dValue(e, totient):
    d = 2
    while(1):
        if((d*e) % totient) == 1:
            break
        d += 1
    return d

def genPubPrivKey():
    p = primeNumber(100, 500)
    q = primeNumber(100, 500)

    if (p != q):
        n = p*q
        totient = (p-1)*(q-1)
        e = eValue(totient)
        d = dValue(e, totient)
        # pasangan (e,n)
        publicKey = (e,n)
        # pasangan (d,n)
        privateKey = (d,n)
        return (publicKey, privateKey)

print(genPubPrivKey())

#2: Hitung n = p.q