import math 


def list_factors(n):
    factors = [1, n]
    r = math.sqrt(n)
    for k in range(2, int(r)+1):
        if n % k == 0:
            factors.append(k)
            factors.append(n // k)
    return factors

if __name__ == "__main__":
    i = 1
    n = 1
    factors = list_factors(n)
    while len(factors) < 500:
        i += 1
        n += i
        factors = list_factors(n)
    print(n)