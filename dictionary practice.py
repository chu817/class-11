print('STOCK')
s={}
ch=0

while(ch!=7):
    print('\n1.Add products \n2.Display Details based on quantity \n3.Increase unit price \n4.Calculate total quantity of stocks \n5.Display Max and minimum retail price \n6.Total value of stock \n7.Exit')
    ch=int(input("Enter your choice"))
    if (ch==1):
        key=int(input("enter the item code"))
        if key not in s:
            name=input("enter the item name")
            q=int(input("enter the item quantity"))
            p=float(input("enter the price per unit"))
            std=input("enter the stock date (dd-mm-yy)")
            s[key]=[name,q,p,std]
            print('Product has been added')
        else:
            print("Sorry! The product already exists")
    elif(ch==2):
        upperlimit=int(input("enter the amount below which to display"))
        print('Item Code\tItem Name\tQuantity\tPrice\tStock Date')
        for i in s:
            if(s[i][1]<upperlimit):
                print(i,'\t',s[i][0],'\t',s[i][1],'\t',s[i][2],'\t',s[i][3])
    elif(ch==3):
        year=input("enter the year to be checked")
        increase=int(input("enter the percentage to increase the price by"))
        for i in s:
            if(year in s[i][3]):
                s[i][2]=(((100+increase)/100)*s[i][2])
        print("Unit Price successfully updated")
    elif(ch==4):
        tq=0
        for i in s:
            tq+=s[i][1]
        print('Total quantity is:',tq)
    elif(ch==5):
        maximum=0
        minimum=0
        for i in s:
            if(s[i][2]>maximum):
                maximum=s[i][2]
            if(s[i][2]<minimum):
                minimum=s[i][2]
        for i in s:
            if(s[i][2]==maximum):
                print("product with max price:",s[i][0],"/nprice:",maximum)
            if(s[i][2]==minimum):
                print("product with min price:",s[i][0],"/nprice:",minimum)
                
        print("Maximum Unit Price is:",maximum,"\nMinimum Unit Price",minimum)
    elif(ch==6):
        val=0
        x=0
        for i in s:
            value=s[i][1]*s[i][2]
            x+=val
        print('Total stock value is',x)
    elif(ch==7):
        print('Thank You')
        
        
    
                
            
                
            
            
            
            
    
