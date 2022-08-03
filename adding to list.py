l=eval(input("enter the list"))
n=len(l)
print(l)
e=input("enter the element")
pos=int(input("enter the position"))

if(pos<=n):
    l+=[0]
    for i in range(n):
        if(i==pos-1):
            for j in range(n-1,i-1):
                l[j]=l[j-1]
            l[i]=e
        print('New list:',l)
