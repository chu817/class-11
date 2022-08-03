#sum of factorials of n numbers
exitflg = "yes"
while(exitflg=="yes"):

    n=int(input('enter the number'))
    x=0
    for i in range(n,0,-1):
        f=1
        r=i
        for j in range(r,0,-1):
            f=f*j
        x+=f
    print(x,"is the sum of factorials")
    exitflg=input("do you want to continue")

    
