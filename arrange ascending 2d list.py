r1=int(input("enter the number of rows"))
c1=int(input("enter the number of columns"))
L=[[0 for j in range(c1)]for i in range(r1)]
for i in range(r1):
    for j in range(c1):
        print('L[',i,'][',j,']=',end='')
        L[i][j]=int(input())
print()
for i in range(r1):
    for j in range(c1):
        print(L[i][j],end='')
    print()
for i in range(c1):
    for j in range(r1):
        for k in range(j+1,c1):
            if(L[i][k]<L[i][j]):
                L[i][k],L[i][j]=L[i][j],L[i][k]
for i in range(r1):
    for j in range(c1):
        print(L[i][j],end='')
    print()
