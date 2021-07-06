if __name__ == "__main__":
    number = '0'
    for i in range(1,10**6):
        number += str(i)
    print(int(number[1]) * int(number[10]) * int(number[100]) * int(number[1000]) * int(number[10000]) * int(number[100000]) * int(number[1000000]))
