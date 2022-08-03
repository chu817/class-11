r=int(input("enter the number of rowns"))
c=int(input("enter the number of columns"))
L=[[0 for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        print('L[',i,'][',j,']=',end='')
        L[i][j]=int(input())
print()
for i in range(r):
    for j in range(c):
        print(L[i][j],end='')
    print()
    
