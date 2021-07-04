if __name__ == "__main__":
    products = set()
    for a in range(1,100):
        for b in range(1,10000):
            digits = str(a) + str(b) + str(a*b)
            unique_digits = set(digits)
            if len(digits) > 9:
                break
            if len(digits) == 9 and len(unique_digits) == 9 and '0' not in unique_digits:
                products.add(a*b)
    print(sum(products))