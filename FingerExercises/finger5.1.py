def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp > 0:
        result *= base
        exp -=1
    return result

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):
     
    # Your code here
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    else: # exp is odd
        return base * recurPowerNew(base, exp - 1)

def gcdIter(a, b):
    result = min(a,b)
    while result > 0:
        if a % result == 0 and b % result == 0 :
            return result
        else:
            result -= 1
    return result
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0 :
        return a
    else:
        return gcdRecur(b, a % b)
def fib(x):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    length=0
    for c in aStr:
        length += 1

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return 0
    else:
        return  1 + lenRecur(aStr[:-1])

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    else:
        mid = len(aStr)/2
        c = aStr[mid] 
        if c == char:
            return True
        elif c < char:
            return isIn(char, aStr[mid+1:])
        else:
            return isIn(char, aStr[:mid])

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    #print str1, str2

    if len(str1) != len(str2):
        return False
    if len(str1) == 1:
        return str1 == str2
    elif str1 == str2:
        return False
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])




        
        
        


 
    

