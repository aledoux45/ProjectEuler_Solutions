## NOTE: we have to see that in order to get to the 
# bottom right corner, we need to do n steps to the
# right and n steps down in any order
# so the total number of ways is n chooses 2*n

import math

if __name__ == "__main__":
    n = 20
    answer = int(math.factorial(2*n) / (math.factorial(n) * math.factorial(n)))
    print(answer)