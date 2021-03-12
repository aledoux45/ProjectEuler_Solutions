def collatz_chain(n):
    chain = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        chain.append(n)
    return chain

if __name__ == "__main__":
    max_chain = 0
    max_n = 0
    for n in range(1,10**6):
        chain = collatz_chain(n)
        if len(chain) > max_chain:
            max_chain = len(chain)
            max_n = n
    print(max_n)