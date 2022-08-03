l=int(input("Enter the battery level"))
if(l<=20):
    print("low battery")
elif(l>=21 and l<=40):
    print("Battery saver recommended")
elif(l>=41 and l<=70):
    print("Moderate use recommended")
elif(l>=71 and l<=99):
    print("Heavy usage can be done")
else:
    print("Battery full")
