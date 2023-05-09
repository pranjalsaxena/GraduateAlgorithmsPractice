import numpy as np

def penalty(x, y):
    return pow((200 - (y-x)),2)

def maxProfit(M, P, k):
    n = len(M)
    T = [0] * n

    maxt = 0
    for i in range(n):
        if (M[i] <= k):
            T[i] = P[i]
        else:
            maxt = 0
            for t in reversed(range(i)):
                if ((M[i]-M[t]) >= k):
                    if (T[t] > maxt):
                        maxt = T[t]
            T[i] = maxt + P[i]

    return max(T)

profit = maxProfit([100, 250, 300, 400, 500, 600, 750], [500, 600, 300, 700, 800, 400, 900], 150)

print (profit)

# input [100, 200, 300, 400, 500, 600, 700], [500, 600, 300, 700, 800, 400, 900], 150
# output 2500

# input [100, 200, 300, 400, 500, 600, 750], [500, 600, 300, 700, 800, 400, 900], 150
# output 2600

# input [100, 250, 300, 400, 500, 600, 750], [500, 600, 300, 700, 800, 400, 900], 150
# output 3100