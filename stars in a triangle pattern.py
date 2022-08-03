n=int(input("n:"))
for i in range(n,0,-1):
    for k in range(i,n):
        print(end=" ")
    for j in range(1,i+1):
        print('*',end='')
    print()

