print('Sprinters')
s={}
ch=0

while(ch!=7):
    print('\n1.Add Athlete \n2.Display Athletes from a country \n3.Delete an athlete based on venue \n4.Athlete rank \n5.Athlete speeds \n6.Exit')
    ch=int(input("Enter your choice"))
    if (ch==1):
        name=int(input("enter athlete name"))
        if key not in s:
            rank=input("enter the rank")
            time=float(input("enter the top time"))
            country=float(input("enter country"))
            date=input("enter the date of event(dd-mm-yy)")
            venue=input("enter the venue")
            s[name]=[rank,time,country,date,venue]
            print('Athlete has been added')
        else:
            print("Athlete is already part of the register")
    elif(ch==2):
        uh=input("Enter the country from whose athletes are to be displayed")
        for i in s:
            if(s[i][2]==uh):
                print(i,'\t',s[i][0],'\t',s[i][1],'\t',s[i][2],'\t',s[i][3],'\t',s[i][4])
    elif(ch==3):
        n=input("enter the venue records to be deleted")
        for i in s:
            if(s[i][4]==n):
                del s[i]
            print("the record has been updated")
    elif(ch==4):
        n=input("enter athlete name")
        if n in s:
            print(n,',rank no.',s[n][0])
    elif(ch==5):
        count=0
        su=0
        for i in s:
           count+=1
           su+=s[i][1]
        print(su/count)
    elif(ch==6):
        print('Thank You')
    elif(ch==7):
        print("i hate this family")
        print("they are so horrible")
        print("i wish i could leave")
        
