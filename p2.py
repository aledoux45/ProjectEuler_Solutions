if __name__ == "__main__":
    f1 = 1
    f2 = 1
    f = f1 + f2
    answer = 0
    
    while f < 4*10**6:
        if f % 2 == 0:
            answer += f
        f1 = f2
        f2 = f
        f = f1 + f2
    print(answer)