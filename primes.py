while True:
    n = int(input('Enter a number: '))

    fact_n = 1
      
    for i in range(1,n): 
        fact_n = fact_n * i 

  
    if (fact_n+1)%n**2==0 and n!=1: 
       print(n,' is a Wilson prime')
    elif (fact_n+1)%n==0 and n!=1:
       print(n,' is prime')     
    else:
       print(n,' is not prime')