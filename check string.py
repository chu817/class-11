n=input("enter a string")
a=input("enter chr to be checked")
c=0
for i in n:
    if i==a:
        c+=1
print(a,"is present",c,"times in",n)
    
