print("program 1:pyramid","program 2: inverted pyramid","program3:hollow pyramid","program 4:inverted hollow pyramid","program5: diamond")
ch=int(input("enter the code number"))
n=int(input("etner the no.of steps"))
if(ch==1):
 for i in range(1,n+1):
    for k in range(i,n):
        print(end=" ")
    for j in range(1,2*i):
        print('*',end='')
    print()
elif(ch==2):
 for i in range(n,0,-1):
    for k in range(i,n):
        print(end=" ")
    for j in range(1,2*i):
        print('*',end='')
    print()
elif(ch==3):
 for i in range(1,n+1):
    for k in range(i,n):
        print(end=" ")
    for j in range(1,2*i):
        if(j==1 or j==2*i-1 or i==n):
           print('*',end='')
        else:
            print(end=' ')
    print()
elif(ch==4):
 for i in range(n,0,-1):
    for k in range(i,n):
        print(end=" ")
    for j in range(1,2*i):
        if(j==1 or j==2*i-1 or i==n):
           print('*',end='')
        else:
            print(end=' ')
    print()
elif(ch==5):
 for i in range(1,n+1):
    for k in range(i,n):
        print(end=" ")
    for j in range(1,2*i):
        if(j==1 or j==2*i-1):
            print('*',end='')
        else:
            print(end=' ')
    print()
    for p in range(n-1,0,-1):
        for q in range(p,n):
            print(end=" ")
        for r in range(1,2*p):
            if(j==1 or j==2*p-1):
               print('*',end='')
            else:
             print(end=' ')
    print()
