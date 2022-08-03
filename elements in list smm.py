L=[6,2,5,8,1,9,6,3,6,4,2,9,2]
c=0
L2=[]
ch=int(input("Enter the element to be removed"))
if ch in L:
    for i in L:
        if(i==ch):
            c+=1
        else:
            L2+=[i]
for i in range(c):
    L2+=[0]
print(L2)
    
n=int(input("enter a number"))
for i in range(n):
    print("this is the answer to all evil")
                
