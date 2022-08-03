u=int(input("enter the units used"))
if (u<=50):
    print("the cost is 0")
elif(u>=51 and u<=100):
    print("the cost is",0.6*u)
elif(u>=101 and u<=200):
    print("the cost is" ,0.75*u)
elif(u>=201 and u<=300):
    print("the cost is ",0.9*u)
elif(u>=300):
    print("the cost is ",1.15*u)
    
