import math


def isprime(n):
    """
    Check is a number is prime
    Note: since all primes > 3 are of the form 6n ± 1
    then start with k=5 (which is prime)
    and test k, k+2 for being prime
    then loop by 6. 
    """
    # Special cases
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    # Loop by 6
    r = math.sqrt(n)
    k = 5
    while k <= r:
        if n % k == 0: 
            return False
        if n % (k+2) == 0: 
            return False
        k += 6
    return True


def prime_factors(n):
    prime_factors = []
    if n % 2 == 0:
        prime_factors.append(2)
        k1 = n // 2
        if isprime(k1):
            prime_factors.append(k1)
    r = math.sqrt(n)
    for k in range(3, int(r)+1, 2):
        if n % k == 0:
            if isprime(k):
                prime_factors.append(k)
            k1 = n // k
            if isprime(k1):
                prime_factors.append(k1)
    return prime_factors

def prime_factors(n):
    factors = []
    for k in range(2,int(math.sqrt(n))+1):
        if n % k == 0 and k**2 != n:
            factors.append(k)
            factors.append(n//k)
        elif k**2 == n:
            factors.append(k)
    prime_factors = [p for p in factors if isprime(p)]
    return prime_factors

if __name__ == "__main__":
    res = prime_factors(600851475143)
    print(max(res))