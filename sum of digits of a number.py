n=int(input("enter a number"))
t=n
c=0
while(t!=0):
    c+=(t%10)
    t=t//10
print("the sum of the digits of",n,"is",c)
