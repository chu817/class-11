print('Matrix-A')
r1=int(input('enter number of rows'))
c1=int(input('enter number of columns'))
A=[[0 for j in range(c1)]for i in range(r1)]
print('Enter the values for matrix A')
for i in range(r1):
    for j in range(c1):
        print('A[',i,'][',j,']:')
        A[i][j]=int(input())
print('Matrix-B')
r2=int(input('enter number of rows'))
c2=int(input('enter number of columns'))
B=[[0 for j in range(c2)]for i in range(r2)]
print('Enter the values for matrix B')
for i in range(r2):
    for j in range(c2):
        print('A[',i,'][',j,']:')
        B[i][j]=int(input())

print('Matrix additio of A and B')
if(r1==r2 and c1==c2):
    for i in range(r2):
        for j in range(c2):
            print(A[i][j]+B[i][j],end='')
        print()
else:
    print('Matrix addition is not possible')
