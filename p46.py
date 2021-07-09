from p7 import list_primes
from p39 import is_perfect_square

def p46():
    primes = set(list_primes(10**6))
    n = 3
    while True:
        if n not in primes:
            found = False
            for p1 in list_primes(n):
                if is_perfect_square((n - p1)//2):
                    found = True
                    break
            if not found:
                return n
        n += 2

if __name__ == "__main__":
    print(p46())