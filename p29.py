if __name__ == "__main__":
    numbers = set()
    max_a = 100
    max_b = 100
    for a in range(2, max_a+1):
        for b in range(2, max_b+1):
            numbers.add(a**b)
    print(len(numbers))