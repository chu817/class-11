n=int(input("enter the year"))
if(n%4)==0:
    if (n%100)==0:
        if(n%400)==0:
            print(n,"is a leap year")
        else:
            print(n,"is not a leap year")
    else:
        print(n,"is a leap year")
else:
     print(n,"is not a leap year")
