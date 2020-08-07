def aproximate(i, list, list2):
    n = 2
    cord = 0
    out = 0
    temp = 0
    while True: 
        cord = []   
        aprx = i**(1/(3**n))  
        for val in range(1, n):
            #print('Im here')
            cord.append(int(aprx**(3**val)))
        a = set(list)
        b = set(cord)
        result = a.union(b)
        #print(i, result,a,b)
        if result==a: 
            #print('now im here')
            temp = aprx
        else:
             out = 1
        if out == 1:
            break
        if n > list2[0]: 
            #print('and im finally here')
            list2[0] = n
            temp = float(temp)
            list2[1] = temp       
        n += 1     
try:
    theta = [0,0]
    primes = [2]
    i = 3 
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
           aproximate(i, primes, theta)
        i+=1
finally:
    print('Theta is aproximetly equal to: ',theta[1])