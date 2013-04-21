#finger 6.1.py
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    rTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            rTup += (aTup[i],)
    return rTup

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = None
    for k in aDict:
        result += len(aDict[k])
    return result

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = 0
    biggest = None
    for k in aDict:
        if len(aDict[k]) >= result: # max
            result = len(aDict[k])
            biggest = k
    return biggest

                     



        
