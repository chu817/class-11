h=int(input("enter the hour in HH format"))
m=int(input("enter the minutes in MM format"))
if(h>12):
    h-=12
    print("the time is",h,':',m,"PM")
elif(h==12):
    print("the time is",h,':',m,"PM")
else:
    print("the time is",h,':',m,"AM")
    
