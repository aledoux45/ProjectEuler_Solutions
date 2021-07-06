import math

if __name__ == "__main__":
    numbers = []
    for k in range(10,100000):
        if sum(math.factorial(int(d)) for d in str(k)) == k:
            numbers.append(k)
    print(sum(numbers))