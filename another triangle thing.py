n=int(input("enter the number of lines"))
for i in range(1,n+1):
    if(i%2==0):
        for k in range(i+1,1,-1):
            print("$",end="")
    else:
        for j in range(1,i+1):
            print(j,end="")
    print()
