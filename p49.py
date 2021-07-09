from p3 import isprime
from p7 import list_primes

def ispermutation(n1, n2):
    digits_n1 = list(str(n1))
    digits_n2 = list(str(n2))
    digits_n1.sort()
    digits_n2.sort()
    if digits_n1 == digits_n2:
        return True
    return False

def p49():
    primes = list_primes(10000)
    set_primes = set(primes)
    for p in primes:
        for k in range(2,(10000-p)//2+1,2):
            if p != 1487 and p+k in set_primes and p+2*k in set_primes and ispermutation(p,p+k) and ispermutation(p,p+2*k):
                answer = str(p)+str(p+k)+str(p+2*k)
                return answer

if __name__ == "__main__":
    print(p49())