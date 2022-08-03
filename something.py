n=int(input("n"))
for i in range(1,n+1):
    if (i%2==0):
        for j in range(1,i):
            print("#",end='')
    else:
        for j in range(1,i):
            print(j,end='')
    print()
5
