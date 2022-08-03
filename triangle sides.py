x=int(input("enter the length of side 1"))
y=int(input("enter the length of side 2"))
z=int(input("enter the length of side 3"))
flag=0
if(x==y and y==z):
    print("equilateral triangle")
    flag=1
elif(x==y or y==z or z==x and flag==0):
    print("isosceles triangle")
else:
    print("scalene triangle")
    
    
