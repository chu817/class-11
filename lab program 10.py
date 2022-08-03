#Lab program 9
n=input("enter a string")
x=0
y=0
z=0
a=1
b=0
for i in n:
    if i>='A' and i<='Z' or (i>='a' and i<='z'):
        if i>='A' and i<='Z':
            x=x+1
        if i in "AEIOUaeiou":
            y+=1
    elif i>='0' and i<='9':
        z+=1
    elif i==' ':
        a+=1
    elif i!=' ':
        b+=1
print(x,y,z,a,b)

        
        
        
