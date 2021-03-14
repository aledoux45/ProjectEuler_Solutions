from p12 import list_factors


if __name__ == "__main__":
    # find abundant numbers <= 28123
    abundants = []
    for n in range(1,28124):
        divisors = sum(list_factors(n)) - n
        if divisors > n:
            abundants.append(n)
    # sum of abundant numbers
    sum_abundants = set()
    for i in range(0,len(abundants)):
        for j in range(i,len(abundants)):
            if abundants[i] + abundants[j] < 28124:
                sum_abundants.add(abundants[i] + abundants[j])
            else:
                break
    # find answer
    answer = 0
    for i in range(1,28124):
        if i not in sum_abundants:
            answer += i
    print(answer)