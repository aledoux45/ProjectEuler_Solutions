if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    n_ways = [0 for _ in range(201)]
    n_ways[0] = 1
    for c in coins:
        for i in range(len(n_ways)):
            if i - c >= 0:
                n_ways[i] += n_ways[i - c] 
    print(n_ways[-1])