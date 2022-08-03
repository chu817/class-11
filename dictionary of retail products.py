'''                       RETAIL PRODUCT CATALOG
AIM: To write a python program to perform the dictionary operations for retail product catalog(Product name and price), to append, update,delete and display all the products

'''
r={}
ch=0
while(ch!=5):
    print('\n1.Append \n2.Update \n3.Delete \n4.Display all \n5.Exit')
    ch=int(input('Enter your choice:'))
    if(ch==1):
        n=input('Enter the new product name:')
        if(n not in r):
            p=float(input('Enter the price of the product'))
            r[n]=p
            print('Prod added successfully')
        else:
            print('product already exists!!')

    elif(ch==2):
        x=input('Enter the product name to update the price:')
        if(x in r):
            y=float(input('Enter the new price of the product:'))
            r[x]=y
            print('Price updated sucessfully')
        else:
            print('Product does not exist!! add product to update it\'s price')

    elif(ch==3):
        x=input('Enter the product name to be deleted')
        if(x in r):
            print(r.pop(x)) #del r[x]
        else:
            print('Product does not exist!!!')

    elif(ch==4):
        print('----------------')
        print('Product\tPrice')
        print('----------------')
        for i in r:
            print(i,'\t',r[i])
        print('----------------')

    elif(ch==5):
        print('Thank you')
