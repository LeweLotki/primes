help = int(input('Enter a number: '))

i = 2
n = 7
i = str(i)
i = i*help
help -= 1
n = str(n)
n = n*help
i = int(i)
n = int(n)
n = i+n

list_steps=[0,0]

def split(temp, i, list_steps):
    temp = str(temp)
    temp = list(temp)
    a = 1
    cord = 0
    steps = 1
    for val in range(0, len(temp)-1):
        temp[val]=int(temp[val])
    for val in range(0,len(temp)):
        a*=int(temp[val])
        if temp[val]==4 or temp[val] == 5 or temp[val] == 1 or temp[val] == 3:
           cord = 1
    while a > 9:
        if cord == 1:
           break
        steps+=1    
        temp = a
        a = 1
        temp = str(temp)
        temp = list(temp)
        for val in range(0, len(temp)-1):
            temp[val]=int(temp[val])
        for val in range(0,len(temp)):
            a*=int(temp[val])
    if steps > list_steps[0]:
       list_steps[0]=steps
       list_steps[1]=i

try:  
   while i<=n:
        temp = i  
        split(temp, i, list_steps)
        i+=1
finally:

    print('\n The highest number of steps: ',list_steps[0],'\n number with the highest number of steps: ',list_steps[1])