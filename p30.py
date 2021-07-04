if __name__ == "__main__":
    numbers = []
    n = 1000000
    for i in range(2, n):
        if sum(int(k)**5 for k in str(i)) == i:
            numbers.append(i)
    print(sum(numbers))