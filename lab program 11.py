#lab program 11
x=int(input("enter a number"))
n=int(input("enter the number of terms"))
s=0
k=1
for i in range(1,n+1):
    f=1
    for i in range(1,k+1):
        f=f*i
    s+=(x/f)
    k+=2
print(s,"is the sum of the series")

        
    
