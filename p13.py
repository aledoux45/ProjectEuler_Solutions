def read_numbers(file):
    numbers = []
    for line in open(file):
        number = int(line.strip())
        numbers.append(number)
    return numbers

if __name__ == "__main__":
    numbers = read_numbers("data/p13_numbers.txt")
    total = sum(numbers)
    answer = str(total)[:10]
    print(answer)