n=int(input("enter a number"))
y=0
for i in range(2,n):
    if (n%i==0):
        y+=1
        print(n, "is not a prime number")
        break
if (y==0):
    print(n,"is a prime number")

