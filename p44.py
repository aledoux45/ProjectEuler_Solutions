import math

def ispentagonal(n):
    if n<0:
        return False
    delta=1+24*n
    if int(math.sqrt(delta))**2==int(delta):
        if (1+int(math.sqrt(delta)))%6==0:
            return True
    return False            

def p44():
    i=1
    while True:
        for j in range(i,1,-1):
            if ispentagonal(i*(3*i-1)/2+j*(3*j-1)/2) and ispentagonal(i*(3*i-1)/2-j*(3*j-1)/2):
                answer = int(i*(3*i-1)/2-j*(3*j-1)/2)
                return answer
        i += 1

if __name__ == "__main__":
    print(p44())