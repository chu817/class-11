n=int(input("enter a number"))
m=n
for i in range(1,n):
    n=n*i
if (n==0):
    n=1
print("the factorial of",m,"is",n)
