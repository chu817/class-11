n=int(input("enter your number"))
t=n
c=1
if t!=0:
    t=t//10
    c+=1
if(((n**2-n)%(10^c))!=0):
    print(n,"is not an automorphic number")
else:
    print(n,"is an automorphic number")
