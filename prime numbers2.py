n=int(input("enter a number to check if it is a prime number"))
x=0
if n==2:
    print(n," is a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            x+=1
            print(n,"is not a prime number")
            break
    if x==0:
        print(n,"is a prime number")
    
