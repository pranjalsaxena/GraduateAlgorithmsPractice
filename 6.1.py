import numpy as np
def maxSumSubsequence(S):
    n = len(S)
    T = [0] * n
    K = [0] * n

    T[0] = S[0]
    K[0] = 0
    for i in range(1, n):
        if T[i-1] >= 0:
            T[i] = T[i-1] + S[i]
            K[i] = K[i-1]

        else:
            T[i] = S[i]
            K[i] = i
    
    
    endindex = np.argmax(T)
    startindex = K[endindex]

    return S[startindex:endindex+1], max(T)

ss, sum = maxSumSubsequence([5,15,-30, 10, -5, 40, 10, -56, 1, 2, 3])

print (ss)
print (sum)

# input 5,15,-30, 10, -5, 40, 10
# output [10, -5, 40, 10], 55

# input 5,15,-30, 10, -5, 40, 10, -55, 70, 80
# output [10, -5, 40, 10, -55, 70, 80], 150

# input 5,15,-30, 10, -5, 40, 10, -56, 1, 2, 3
# output [10, -5, 40, 10], 55