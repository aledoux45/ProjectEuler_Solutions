def decimal_cycle(n):
    
if __name__ == "__main__":
    max_cycle = 0
    max_n = 0
    for n in range(1,1000):
        cycle = decimal_cycle(n)
        if len(cycle) > max_cycle:
            max_cycle = len(cycle)
            max_n = n
    print(max_n)