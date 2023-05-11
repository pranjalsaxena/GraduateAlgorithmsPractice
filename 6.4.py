import numpy as np

def dict(word):
    if word in ['my', 'dictionary', 'it', 'was', 'the', 'best', 'of', 'times', 'hello', 'elephant', 'this', 'is', 'a', 'good', 'input']:
        return True
    else:
        return False

def isStringValid(S):
    n = len(S)
    T = [False] * n

# write a loop initializing all elements in T to false
    for i in range(n):
        T[i] = False
    
    for i in range(n):
        if (dict(S[0:i+1])):
            # set T[i] to true
            T[i] = True
        else:
            for t in reversed(range(i)):
                if (T[t] and dict(S[t+1:i+1])):
                    T[i] = True
                    break
    if (T[n-1]):
        sentence = ""
        for i in range(n-1):
            sentence = sentence + S[i]
            if (T[i] and T[i+1] == False):
                sentence = sentence + " "

        return T[n-1], sentence + S[n-1]
    
    else:
        return T[n-1], "Invalid String"


valid, sentence = isStringValid("mydictionaryhelloelephantthis")

print(valid)
print(sentence)

# input "mydictionary"
# output True, my dictionary

# input "mydictionaryhel"
# output False, Invalid String

# input "mydictionaryhelloelephantthis"
# output True, my dictionary hello elephant this