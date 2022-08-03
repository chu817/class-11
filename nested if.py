a=input("enter a number")
b=input("enter another number")
c=input("enter the last number")
if(a>b):
    if(a>c):
        print(a,"is the greatest number")
    elif(a==c):
        print(a,"is the greatest number")
    elif(a<c):
        print(c,"is the greatest number")
elif(b>a):
    if(b>c):
        print(b,"is the greatest number")
    elif(b==c):
        print(b,"is the greatest number")
    else:
        print(c,"is the greatest number")
elif(a==b and a==c):
    print(a,"is the greatest number")
    
