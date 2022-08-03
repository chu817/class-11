l=eval(input("enter the list"))
print(l)
n=int(input("enter the element"))
e=int(input("enter the position"))
x=len(l)-1
l2=[]
for i in range(0,len(l)):
    if(i==e-1):
        l2+=[n]
        p=l[i]
        l2+=[p]
    else:
        x=l[i]
        l2+=[x]
if(e>=x+1):
    for j in range(x+1,e):
        l2+=[]
    l2+=[n]
print(l2,"is the modified list")
    
