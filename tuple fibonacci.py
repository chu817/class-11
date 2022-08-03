n=int(input("enter a number"))
t=()
a=-1
b=1
for i in range(n):
    c=a+b
    t+=(c,)
    a=b
    b=c
print(t)
