from p3 import prime_factors

if __name__ == "__main__":
    n = 10
    while len(prime_factors(n)) != 4 or len(prime_factors(n+1)) != 4 or len(prime_factors(n+2)) != 4 or len(prime_factors(n+3)) != 4:
        n += 1
    print(n)