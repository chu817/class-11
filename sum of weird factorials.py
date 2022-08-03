#s=x/1!+x/4!.....x/3n+1!

exitflg = "yes"
while(exitflg=="yes"):
    n=int(input('enter the number of terms'))
    x=int(input("enter the number"))
    s=0
    for i in(0,n-1):
        f=1
        p=3*i+1
        for j in range(p,0,-1):
                 f=f*j
        s=s+(x/f) 
    print(s,"is the sum of the series")
    exitflg=input("do you want to continue")
