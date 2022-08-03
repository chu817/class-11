l=eval(input("enter the list"))
print(l)
n=int(input("enter the element to be deleted"))
l2=[]
for i in range(0,len(l)):
    if(l[i]==n):
        print(n,"has been deleted")
        break
    else:
        x=l[i]
        l2+=[x]

if(n not in l):
    print(n,"is not an element in",l)
    
print(l2,"is the final list") 
