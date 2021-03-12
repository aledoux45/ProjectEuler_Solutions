## NOTE: we know from the prime number theorem 
# that the number of primes <= N is N / log(N)

import math

def list_primes(n):
    """
    Returns the list of primes below n
    """
    isprime = [False, False, True] + [True, False] * ((n-1) // 2)
    if n % 2 != 0:
        isprime = isprime[:-1]
    r = math.sqrt(n)
    for k in range(3, int(r)+1, 2):
        if isprime[k]:
            k1 = 2
            while k1*k <= n:
                isprime[k1*k] = False
                k1 += 1
    list_p = [i for i, k in enumerate(isprime) if k]
    return list_p


if __name__ == "__main__":
    i = 10001
    n = i
    while n / math.log(n) < i*1.1:
        n += 1
    list_p = list_primes(n)
    print(list_p[i-1])