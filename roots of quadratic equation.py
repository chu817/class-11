a=int(input("enter coefficient of x^2"))
b=int(input("enter coefficient of x"))
c=int(input("enter constant"))
if(b**2-(4*a*c)>0):
    print("real and distinct roots")
if(b**2-(4*a*c)==0):
    print("real and equal roots")
if(b**2-(4*a*c)<0):
    print("imaginary")

