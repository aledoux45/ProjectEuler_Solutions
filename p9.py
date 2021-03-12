## NOTE: a Pythagorean triplet can be written:
# a = m^2 - n^2, b = 2*m*n, c = m^2 + n^2
# where m > n > 0

def pythagorea_triple():
    m = 0
    while True:
        m += 1
        for n in range(1,m):
            k = 1
            a = k*(m**2 - n**2)
            b = k*2*m*n
            c = k*(m**2 + n**2)
            while a + b + c < 1000:
                k += 1
                a = k*(m**2 - n**2)
                b = k*2*m*n
                c = k*(m**2 + n**2)
            if a + b + c == 1000:
                return a*b*c


if __name__ == "__main__":
    res = pythagorea_triple()
    print(res)
