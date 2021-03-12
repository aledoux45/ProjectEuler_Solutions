if __name__ == "__main__":
    number = 2**1000
    answer = sum(int(i) for i in str(number))
    print(answer)