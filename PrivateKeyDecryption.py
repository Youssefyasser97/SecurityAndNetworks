from math import *
def factorizeN(n):
    p ,q = 0, 0
    # you can change the initial values depending on your implementation

    # Your Implementation Here
    return p, q

def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            if n%p == 0:
                break
    myP = p
    myQ = n//p
    Euiler = (myP - 1) * (myQ - 1)
    return(myP,myQ, Euiler)
def euclid_algo(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return  x

def findD(n, e):
    d = 0
    p1,q1,euiler = SieveOfEratosthenes(n)
    d = euclid_algo(e, euiler)
    # Your Implementation Here
    return d

def decrypt(n, d, c):
    m = ( c ** d ) % n
    # Your Implementation Here
    return m

if __name__ == "__main__":
    d = findD(143, 11)
    print("The PrivateKey d is: ", d)
    print("The decrypted message is: ", decrypt(143, d, 106))

    d1 = findD(91, 5)
    print("The PrivateKey d is: ", d1)
    print("The decrypted message is: ", decrypt(91, d1, 9))

    d2 = findD(391, 15)
    print("The PrivateKey d is: ", d2)
    print("The decrypted message is: ", decrypt(391, d2, 364))
