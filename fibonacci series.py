n=int(input("enter a number"))
a=-1
b=1
for i in range(n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
