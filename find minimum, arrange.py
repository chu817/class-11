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
m=L[1][1]
for i in range(r1):
    for j in range(c1):
        if(L[i][j]<m):
            m=L[i][j]
print(m,"is the minimum value")
for i in range(r1):
    if(i%2==0):
        for j in range(c1):
            print(L[i][j],end='')
    else:
        for j in range(c1-1,-1,-1):
            print(L[i][j],end='')
