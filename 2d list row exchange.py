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
if(r1%2==0):
    for j in range(c1):
        L[(r1/2)-1][j],L[r1/2][j]=L[r1/2][j],L[(r1/2)-1][j]
    for i in range(r1):
        for j in range(c1):
            print(L[i][j],end='')
        print()
else:
    print("the number of rows is odd")
if(c1%2==0):
    x=c1//2
    for j in range(r1):
        L[j][x-1],L[j][x]=L[j][x],L[j][x-1]
    for i in range(r1):
        for j in range(c1):
            print(L[i][j],end='')
        print()
else:
    print("the number of columns is odd")
