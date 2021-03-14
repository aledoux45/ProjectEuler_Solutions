def read_triangle(file):
    triangle = []
    for line in open(file):
        triangle.append([int(i) for i in line.strip().split(" ")])
    return triangle

if __name__ == "__main__":
    triangle = read_triangle("data/p18_triangle.txt")
    n_rows = len(triangle)
    max_path = triangle[-1]
    for i in range(n_rows-2, -1, -1):
        local_max = [max(max_path[k-1], max_path[k]) for k in range(1,len(max_path))]
        max_path = [local_max[k] + triangle[i][k] for k in range(len(local_max)) ]
    print( max_path[0] )