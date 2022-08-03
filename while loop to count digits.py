r="yes"
while(r=="yes"):
 n=int(input("enter a number"))
 t=str(n)
 c=0
 while (n!=0):
      n=n//10
      c=c+1
 print("the number of digits that",t,"has is",c)
 r=input("do you want to continue(yes/no)")
