def genPrimes():
    primes = []
    n = 2
    yield n
    primes.append(n)
    n +=1 

    while True:
        prime = True
        for divisor in primes:
            if n % divisor == 0:
                prime = False
                break
        if prime == False:
            n += 2
        else:
        # n shou5ld be prime
            primes.append(n)
            yield n


        

    
    
