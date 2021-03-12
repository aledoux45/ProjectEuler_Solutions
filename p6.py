## NOTE: we know that (x1 + x2 + ... + xn)^2 = 
# x1^2 + x2^2 + ... + xn^2 + 2*sum(xi * xj) (i<j)

if __name__ == "__main__":
    res = 0
    for i in range(1,101):
        for j in range(i+1, 101):
            res += 2*i*j
    print(res)