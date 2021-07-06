from p3 import isprime
from p7 import list_primes

def left_truncate(n, r):
    return int(str(n)[r:])    

def right_truncate(n, r):
    return int(str(n)[:-r])

if __name__ == "__main__":
    list_p = list_primes(10**6)
    numbers = []
    for p in list_p:
        for r in range(1,len(str(p))):
            new_p1 = left_truncate(p, r)
            new_p2 = right_truncate(p, r)
            if not isprime(new_p1) or not isprime(new_p2):
                break
            elif r == len(str(p)) - 1:
                numbers.append(p)
    print(sum(numbers))