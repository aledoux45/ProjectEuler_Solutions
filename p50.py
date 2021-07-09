from p7 import list_primes

if __name__ == "__main__":
    N = 10**6
    primes = list_primes(N)
    set_primes = set(primes)
    max_j = -1
    for i in range(len(primes)):
        j = 1
        consecutive_sum = sum(primes[i:(i+j)])
        while consecutive_sum < N and i+j <= len(primes):
            if consecutive_sum in set_primes and j > max_j:
                max_j = j
                answer = consecutive_sum
            j += 1
            consecutive_sum = sum(primes[i:(i+j)])
    print(answer)