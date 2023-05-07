import numpy as np

def penalty(x, y):
    return pow((200 - (y-x)),2)

def optimalHotelStops(S):
    n = len(S)
    T = [0] * n
    K = [0] * n

    T[0] = penalty(0, S[0])
    K[0] = -1
    for i in range(1, n):
        min = penalty(0, S[i])
        argmin = -1
        for j in range(0, i):
            jtoiPenalty = penalty(S[j], S[i])
            if((jtoiPenalty+T[j]) < min):
                min = jtoiPenalty+T[j]
                argmin = j
        T[i] = min
        K[i] = argmin
    
    #print (T)
    #print (K)

    p = n - 1
    optPath = []
    while(p >= 0):
        optPath.append(S[p])
        p = K[p]
    
    optPath.reverse()

    return optPath, T[n-1]

os, totalPenalty = optimalHotelStops([100, 200, 400, 500, 600, 700, 750, 800, 850, 900, 1000])

print (os)
print (totalPenalty)

# input 100, 200, 500, 950, 1800, 2250, 2500
# output [200, 500, 950, 1800, 2250, 2500], 560000

# input 100, 200, 500, 600, 700, 750, 850, 900, 1000
# output [200, 500, 750, 1000], 15000

# input 100, 200, 400, 500, 600, 700, 750, 800, 850, 900, 1000
# output [200, 400, 600, 800, 1000], 0