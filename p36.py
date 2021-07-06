from p4 import ispalindrome


def to_binary(n):
    """
    Convert a number to binary representation
    and removes leading zeros
    """
    binary = str(bin(n))[2:]
    return int(binary)


if __name__ == "__main__":
    answer = 0
    for k in range(1,10**6):
        bin_k = to_binary(k)
        if ispalindrome(k) and ispalindrome(bin_k):
            answer += k
    print(answer)