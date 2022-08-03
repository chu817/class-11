#finding a reverse
n=int(input("enter a number"))
t=n
s=0
while(t!=0):
    s=(s*10)+(t%10)
    t=t//10
print("the reverse is",s)
