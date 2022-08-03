n=int(input("enter the number of rows"))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end='')
    print()
n=int(input("enter the number of rows"))
for i in range(n):
    ch=ord('A')
    for j in range(i+1,0,-1):
        print(chr(ch),end='')
        ch+=1
    print()
n=int(input("enter the number of rows"))
for i in range(n):
    for k in range(i+1):
        print(' ',end='')
    for j in range(1,(n-i)+1):
        print(j,end='')
    print()

n=int(input("enter the number of rows"))
for i in range(n):
    for k in range(0,2*i+1):
        print(' ',end='')
    for j in range(1,2*((n-i))):
        print(j,end='')
    print()
n=int(input("enter the number of rows"))
for i in range(n):
    ch=ord('A')
    for j in range(i,-1,-1):
        print(chr(ch+j),end='')
    print()
n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for k in range(n-i):
        print(end=' ')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()
n=int(input("enter the number of rows"))
for i in range(n):
    for k in range(n,i,-1):
        print(k,end='')
    for j in range(i):
        print('  ',end='')
    for j in range(i+1,n+1):
        print(j,end='')
    print()
    


