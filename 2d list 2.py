print('Matrix-A')
r1=int(input('enter number of rows'))
c1=int(input('enter number of columns'))
A=[[0 for j in range(c1)]for i in range(r1)]

print('Enter the values for matrix A')
for i in range(r1):
    for j in range(c1):
        print('A[',i,'][',j,']:')
        A[i][j]=input()
for i in A:
    print(i)
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
if(r1==c1):
    for i in range(r1):
        for j in range(c1):
            if(j<=i):
                print(A[i][j],end='')
            else:
                print(end=' ')
        print()
p=int(input("enter a number"))
for i in range(p):
    p=input("enter a number")
    if p=="eiii":
        ans=input("do you want to know my secret?")
        if ans=="yes":
            print("i want to die:)")
        


