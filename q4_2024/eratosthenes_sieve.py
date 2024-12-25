"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

"""

import time

def get_prime_nums_eratosthenes(N):
    prime = [True for i in range(N+1)]
    p = 2

    while(p*p < N):
        if (prime[p] == True):
            # Update all p's multiples to be non prime
            for i in range(p*p, N+1, p):
                prime[i] = False
        
        p+= 1
    
    primes = []

    for p in range(2, N+1):
        if prime[p] == True:
            primes.append(p)
    return primes

#print(get_prime_nums_eratosthenes(100))

def generate_infinite_primes():
    
    D = {}
    # get the first prime out of the way
    q=2
    while True:
        if q not in D:
            # q is a new prime
            yield q
            D[q*q]= [q]

        else:
            #q is composite
            #D[q] is the list of primes that divide it
            # Since we have reached q, we no longer need it in D, 
            # but we will mark the next multiples of its witnesses
            # to prepare for larger numbers
            for p in D[q]:
                print(p)
                print(q)
                D.setdefault(p + q, []).append(p)
                print(D)
                time.sleep(5)
            del(D[q])

        q += 1

gen_primes = (generate_infinite_primes())
for item in gen_primes:
    print(item)
