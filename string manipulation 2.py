ch=0
while(ch!=6):
    print("\n1.Length \n2.Copy \n3.Concatenation \n4.Reverse \n5.Compare \n6.Exit")
    ch=int(input("enter your choice"))
    if(ch==1):
        s1=input("enter a string")
        x=0
        for i in s1:
            x+=1
        print("string length:",x)
    elif(ch==2):
        s1=input("enter a string")
        s2=s1
        print('string copies from s1 to s2:',s2)
    elif(ch==3):
        s1=input("enter a string")
        s2=input("enter another string")
        s2=s2+s1
        print("the concatenated string is:",s2)
    elif(ch==4):
        s1=input("enter a string")
        x=0
        s2=''
        for i in s1:
            x+=1
        for i in range(x-1,-1,-1):
            s2+=s1[i]
        print("Reversed String:",s2)
    elif(ch==5):
        s1=input("enter a string")
        s2=input("enter another string")
        if(s1==s1):
            print("strings are equal")
        else:
            print("strings are not equal")
    elif(ch==6):
        print("thank you")
    else:
        print('enter a choice between 1 and 6')
