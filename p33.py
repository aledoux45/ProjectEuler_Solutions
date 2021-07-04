import math


def digits_in_common(p, q):
    digits_p = list(str(p))
    digits_q = list(str(q))
    digits_common = set(digits_p) & set(digits_q)
    return list(digits_common)

if __name__ == "__main__":
    numerator_prod = 1
    denominator_prod = 1
    for p in range(10,100):
        for q in range(p+1,100):
            common_digits = digits_in_common(p,q)
            if len(common_digits) == 1 and common_digits[0] != '0':
                common_digit = common_digits[0]
                if str(p)[0] == common_digit:
                    new_p = int(str(p)[1])
                else:
                    new_p = int(str(p)[0])
                if str(q)[0] == common_digit:
                    new_q = int(str(q)[1])
                else:
                    new_q = int(str(q)[0])
                if p * new_q == q * new_p:
                    numerator_prod *= new_p
                    denominator_prod *= new_q
    denominator_prod //= math.gcd(numerator_prod, denominator_prod)
    print(denominator_prod)