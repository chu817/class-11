n=int(input('n:'))
for i in range(1,n+1):
    for k in range(1,n):
        print(end=' ')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()
