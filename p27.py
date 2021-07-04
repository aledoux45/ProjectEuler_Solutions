from p3 import isprime


if __name__ == "__main__":
    max_n = 0
    max_a = 0
    max_b = 0
    for a in range(-999,1000):
        for b in range(-999,1000):
            n = 0
            while isprime(n**2 + a*n + b):
                n += 1
            if n > max_n:
                max_a = a
                max_b = b
                max_n = n
    print(max_a*max_b)