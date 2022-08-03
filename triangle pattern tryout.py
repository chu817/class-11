exitflg=0
while(exitflg==0):
 ch=int(input("enter a choice from 1 to 5"))
 if (ch==1):
   n=int(input("enter the number of rows"))
   for i in range(1,n+1):
        for j in range(0,i):
            print(i,end='')
        print()
   print("thank you")
 elif (ch==2):
    n=int(input("enter the number of rows"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
    print("thank you")
 elif(ch==3):
    k=1
    n=int(input("enter the number of rows"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(k,end='')
            k=k+1
        print()
 elif(ch==4):
    n=int(input("enter the number of rows"))
    for i in range(n):
        c=65
        for j in range(i+1):
            print(chr(c),end='')
            c=c+1
        print()
 elif(ch==5):
    n=int(input("enter the number of rows"))
    for i in range(n):
        c=65
        for k in range(n+1,i,-1):
            print(end=" ")
        for j in range(0,i+1):
            print(chr(c),end='')
            c=c+1
        print()
 elif(ch==6):
    print("thank you")
 else:
    print("enter a number from 1 to 6")
        
    
