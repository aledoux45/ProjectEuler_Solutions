import math

def is_perfect_square(n):
    sq_root = int(math.sqrt(n))
    return (sq_root*sq_root) == n

if __name__ == "__main__":
    count_p = {}
    for a in range(1,1000):
        for b in range(a,1000):
            h2 = a**2 + b**2
            h2_root = int(math.sqrt(h2))
            if h2_root*h2_root == h2:
                perimeter = a + b + h2_root
                triplet = (a,b,h2_root)
                if perimeter <= 1000 and perimeter in count_p:
                    count_p[perimeter].add(triplet)
                else:
                    count_p[perimeter] = set([triplet])
    print(max(count_p, key=lambda x: len(count_p[x])))
