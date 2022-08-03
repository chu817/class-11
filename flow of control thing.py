n=int(input("enter the number of lines"))
for i in range(0,n):
    for j in range(0,n-i):
        print(end=' ')
    for k in range(n-i,n+1,1):
        print(k,end='')
    print('')
       
    
