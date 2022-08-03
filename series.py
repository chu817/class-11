n=int(input("enter the number of terms"))
f=1
for j in range(1,n+1):
        f=f*j
        print(((-1)**(j+1)),"/",f)
