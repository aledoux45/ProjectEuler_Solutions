from p3 import isprime
from p7 import list_primes

def rotate(n,r):
    digits = list(str(n))
    new_n = digits[r:] + digits[:r]
    return int(''.join(new_n))

if __name__ == "__main__":
    list_p = list_primes(10**6)
    numbers = []
    for p in list_p:
        for r in range(len(str(p))):
            new_p = rotate(p, r)
            if not isprime(new_p):
                break
            elif r == len(str(p)) - 1:
                numbers.append(p)

    print(len(numbers))
