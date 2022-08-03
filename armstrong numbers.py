n=int(input("enter a number"))
t=n
s=0
while(t!=0):
    s+=((t%10)**3)
    t=t//10
if(s==n):
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
    
