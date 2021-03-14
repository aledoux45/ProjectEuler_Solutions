from itertools import permutations

if __name__ == "__main__":
    n = 0
    for i in permutations('0123456789',10):
        n += 1
        if n == 1000000:
            print(''.join(i))
            break  