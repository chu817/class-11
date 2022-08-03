n=int(input())
a=-1
b=1
c=0
flag=0
while(c<=n):
    c=a+b
    a=b
    b=c
    if(c==n):
        print("yes")
        flag=1
if flag==0:
    print("no")
    
