if __name__ == "__main__":
    numbers = [n**n for n in range(1,1001)]
    answer = str(sum(numbers))[-10:]
    print(answer)
