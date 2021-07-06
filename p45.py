if __name__ == "__main__":
    n = 10**6
    triangles = set([k*(k+1)//2 for k in range(1,3*n)])
    pentagones = set([k*(3*k-1)//2 for k in range(1,n)])
    hexagones = set([k*(2*k-1) for k in range(1,2*n)])
    inter = triangles & pentagones & hexagones
    answer = [i for i in inter if i > 40755]
    print(answer[0])