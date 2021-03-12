import numpy as np

def read_grid(grid_file):
    grid = []
    for line in open(grid_file):
        line_numbers = [int(i.strip()) for i in line.split(" ")]
        grid.append(line_numbers)
    return np.array(grid)

if __name__ == "__main__":
    grid = read_grid("data/p11_grid.txt")
    n_row, n_col = grid.shape
    n_product = 4
    max_product = 0
    for i in range(n_row):
        for j in range(n_col):
            # Horizontal
            if j < n_col - n_product + 1:
                numbers = grid[i,j:j+n_product]
                prod = np.product(numbers)
                if prod > max_product:
                    max_product = prod
            # Vertical
            if i < n_row - n_product + 1:
                numbers = grid[i:i+n_product,j]
                prod = np.product(numbers)
                if prod > max_product:
                    max_product = prod
            # Diagonal Down
            if i < n_row - n_product + 1 and j < n_col - n_product + 1:
                numbers = [grid[i+k,j+k] for k in range(n_product)]
                prod = np.product(numbers)
                if prod > max_product:
                    max_product = prod
                
            # Diagonal Up
            if i > n_product - 2 and j < n_col - n_product + 1:
                numbers = [grid[i-k,j+k] for k in range(n_product)]
                prod = np.product(numbers)
                if prod > max_product:
                    max_product = prod
    print(max_product)