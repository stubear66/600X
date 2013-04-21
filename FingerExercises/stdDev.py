def stdDev (L):
    n = float(len(L))
    mean = sum(L) / n
    sumDevSquared = 0
    for i in L:
        sumDevSquared += (i - mean) ** 2
    s = (sumDevSquared / n) ** 0.5
    return s



    
