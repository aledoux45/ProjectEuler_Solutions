def ispalindrome(n):
    digits = list(str(n))
    for i in range(len(digits)//2):
        if digits[i] != digits[-1-i]:
            return False
    return True

if __name__ == "__main__":
    max_pal = 0
    for k1 in range(100,1000):
        for k2 in range(100,1000):
            if k1*k2 > max_pal and ispalindrome(k1*k2):
                max_pal = k1*k2
    print(max_pal)
