while True:
    m = []
    n = int(input('Enter a number: '))
    n_a=n
    fact_n = 1     
    for i in range(1,n): 
        fact_n = fact_n * i 
    if  (fact_n+1)%n==0 and n!=1:
        n = list(map(int,str(n)))
        for i in n:
            m.append(i)
        temp = m
        for i in range(1,len(m)):
            temp[-i]=m[i-1]
        i = 0
        m = 0
        for val in temp:
            m+=(10**i)*val
            i+=1
        fact_m = 1
        for i in range(1,m): 
            fact_m = fact_m * i 
        print(m, fact_m)
        if  (fact_m+1)%m==0:
            print(n_a,' is a palindrome prime!')
    else:
        print(n_a,' is not a palindrome prime :(')