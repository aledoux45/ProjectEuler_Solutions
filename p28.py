if __name__ == "__main__":
    # Start with center of the square (=1)
    total = 1
    u = 1
    n = 1001
    for i in range(1, (n-1)//2 + 1):
        # Compute four corners
        u += 8*(i-1)+2
        v = u + 2*i
        w = u + 4*i
        x = u + 6*i
        # Add to total sum
        total += u + v + w + x
    print(total)