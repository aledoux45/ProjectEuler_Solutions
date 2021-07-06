if __name__ == "__main__":
    pandigital = []
    for p in range(1,10**6):
        digits = list(str(p))
        i = 2
        while len(digits) < 10:
            if '0' in digits:
                break
            if len(digits) == 9 and len(digits) == len(set(digits)):
                pandigital.append(int(''.join(digits)))
                break
            digits.extend(list(str(p*i)))
            i += 1
    print(max(pandigital))
