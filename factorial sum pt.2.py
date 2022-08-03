n=int(input("enter the number of terms"))
x=int(input("enter the numerator"))
s=0
for i in range(0,n+1):
    p=3*i+1
    f=1
    for j in range(p,1,-1):
        f=f*j
    s+=(x/f)*((-1)**i)
print("the sum of the series is",s)
    
