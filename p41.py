from p7 import list_primes

def ispandigital(n):
    digits = list(str(n))
    OneToNdigits = [str(i) for i in range(1,len(digits)+1)]
    if sorted(digits) == OneToNdigits:
        return True
    return False

if __name__ == "__main__":
    list_p = list_primes(10**7)
    for p in list_p:
        if ispandigital(p):
            answer = p
    print(answer)