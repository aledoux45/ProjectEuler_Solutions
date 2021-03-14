if __name__ == "__main__":
    f1 = 1
    f2 = 1
    f = f1 + f2
    i = 2
    while len(str(f)) < 1000:
        f = f1 + f2
        f1 = f2
        f2 = f
        i += 1
    print(i)