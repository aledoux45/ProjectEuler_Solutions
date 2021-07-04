def decimal_cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    lpow = 1
    while True:
        for mpow in range(lpow-1,-1,-1):
            if (10**lpow - 10**mpow) % n == 0:
                return lpow - mpow
        lpow += 1
    
if __name__ == "__main__":
    max_cycle = 0
    max_n = 0
    for n in range(1,1000):
        cycle = decimal_cycle(n)
        if cycle > max_cycle:
            max_cycle = cycle
            max_n = n
    print(max_n)