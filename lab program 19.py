book={}
ch=''
while (ch!='E'):
    print('\nL-Librarian \nU-User \nE-Exit')
    ch=input('Enter the Login Character <L/U/E>:')
    if(ch=='L'):
        pwd=input('Enter the password')
        if(pwd=='admin@1234'):
            ch1=0
            while(ch1!=4):
                print("\n\n\t\t*********Library Management System*********")
                print("\n1.Add new \n2.Check Total book \n3.Delete \n4.Exit")
                ch1=int(input('Enter your choice:'))
                if(ch1==1):
                    bid=input("enter the book ISBN:")
                    if(bid not in book):
                        n=input('Enter the book name:')
                        p=float(input("Enter the price:"))
                        y=int(input("enter the publication year:"))
                        book[bid]=[n,p,y]
                        print('Book added successfully')
                    else:
                        print('Book details already exist!!')
                elif(ch1==2):
                    for i in book:
                        print(i,end="\t")
                        t=book[i]
                        for j in t:
                            print(j,end="\t")
                        print()
                    print("\nTotal books:",len(book))
                elif(ch1==3):
                    bk=input("enter the ISBN for the following")
                    if bk in book:
                        del book[bk]
                        print("record deleted")
                    else:
                        print("ISBN not available")
                elif(ch1==4):
                    print("<---- Returning to Main Menu")
        else:
            print('Invalid Password')
    elif(ch=='U'):
        bk=input("Enter the ISBN for searching:")
        if bk in book:
            print("Name, Price, Year")
            print(book[bk])
        else:
            print('ISBN not available')
    elif(ch=='E'):
        print("\n\t Thank You!! Visit Again!!")
        
                
                    
