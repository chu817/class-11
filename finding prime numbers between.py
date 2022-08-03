n=int(input("enter the upper limit"))
m=int(input("enter the lower limit"))
for i in range(m,n+1):
    flag=0
    for j in range(2,i//2):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i,end=" ")
