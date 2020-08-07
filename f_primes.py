primes = [2]
i = 3
try:   
    while True:   
        cord = 0
        for val in primes:
            if val <= i**(1/2):
                if i%val==0:
                   cord = 1
                   break
            else:
                break
        if cord!=1:
           primes.append(i)
        i+=1
finally:
    print('The biggest prime founded: ',primes[-1])
    print('In total ',len(primes),' primes has been founded in range( 0,',i,').')      