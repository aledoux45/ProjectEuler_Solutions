## Note: this problem can be solved manually by saying that the smallest
# number evenly divisible by all numbers from 1 to 20 is the smallest set
# containing all prime factors of all numbers from 1 to 20
# Below is an implementation of this idea

import math
from p3 import isprime


def prime_factors_duplicity(n, factors=[]):
    """
    Returns a list of prime factors with duplicity
    """
    if n < 4 or n == 5 or n == 7:
        return factors + [n]
    if n % 2 == 0:
        factors.append(2)
        return prime_factors_duplicity(n // 2, factors)
    r = math.sqrt(n)
    for k in range(3, int(r)+1, 2):
        if n % k == 0:
            k1 = k
            k2 = n // k
            isp_k1 = isprime(k1)
            isp_k2 = isprime(k2)
            if isp_k1 and isp_k2:
                factors.append(k1)
                factors.append(k2)
                return factors
            elif isp_k1:
                factors.append(k1)
                return prime_factors_duplicity(n // k1, factors)
            elif isp_k2:
                factors.append(k2)
                return prime_factors_duplicity(n // k2, factors)
    return factors + [n]

def count(arr):
    """
    Returns a count of the elements in array
    """
    counts = {}
    for e in arr:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1
    return counts

if __name__ == "__main__":
    count_total = {}
    for k in range(1,21):
        print(k)
        pfact_k = prime_factors_duplicity(k, [])
        print(k, pfact_k)
        count_k = count(pfact_k)
        for c in count_k:
            if c not in count_total:
                count_total[c] = count_k[c]
            elif count_total[c] < count_k[c]:
                count_total[c] = count_k[c]
    res = 1
    for i in count_total:
        res *= i**count_total[i]
    print(res)