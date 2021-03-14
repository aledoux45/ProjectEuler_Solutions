from p12 import list_factors

if __name__ == "__main__":
    total = 0
    for n1 in range(1,10001):
        n2 = sum(list_factors(n1)) - n1
        if n1 != n2 and sum(list_factors(n2)) - n2 == n1:
            total += n1
            total += n2
    print(total // 2)
