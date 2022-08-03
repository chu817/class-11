print('Matrix-A')
r1=int(input('enter number of rows'))
c1=int(input('enter number of columns'))
A=[[0 for j in range(c1)]for i in range(r1)]

print('Enter the values for matrix A')
for i in range(r1):
    for j in range(c1):
        print('A[',i,'][',j,']:')
        A[i][j]=int(input())
print('Diagonal elements')
if(r1==c1):
    for i in range(r1):
        for j in range(c1):
            if(i==j or i+j==r1-1):
                print(A[i][j],end='')
            else:
                print(end=' ')
        print()
else:
    print("not possible")

print("upper triangular matrix")
if(r1==c1):
    for i in range(r1):
        for j in range(c1):
            if(i<=j):
                print(A[i][j],end='')
            else:
                print(end=' ')
        print()
else:
    print("not possible")

print('Sum of the column elements')
s=[]
for i in range(c1):
    s+=[0]
    for j in range(r1):
        s[i]+=A[j][i]
for i in range(r1):
    for j in range(c1):
        print(A[i][j],end=" ")
    print()
print(s,end='')
   
