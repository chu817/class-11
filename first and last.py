n=int(input("enter the number"))
t=n
t2=n
c=0
while(t!=0):
    t=t//10
    c+=1
print((n//(10**(c-1)))*10+(n%10))
