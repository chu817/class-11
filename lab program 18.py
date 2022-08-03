t=()
i=1
ch=0
while(ch!=7):
    print('''\n1.Add new over score \n2.Length(to find number of overs)
3.Slicing(to see specific overs)
4.Concatenation(Adding a few overs)
5.Membership (Checking score card)
6.Count
7.Exit''')
    ch=int(input("enter your choice:"))
    if ch==1:
        print("Enter score for Over",i,':',end='')
        x=int(input())
        t+=(x,)
        i+=1
    elif ch==2:
        print('Number of overs bowled:',len(t))
    elif ch==3:
        y=int(input('Enter the starting over'))
        z=int(input('Enter the ending Over'))
        print(t[y-1:z])
    elif ch==4:
        t2=eval(input('Enter the scores in the tuple'))
        i+=len(t2)
        t=t+t2
        print('New score card',t)
    elif ch==5:
        print('IN')
        x=int(input("Enter the runs to be checked"))
        if x in t:
            for j in range(len(t)):
                if(t[j]==x):
                    print(x,'Runs scored in Over no,',j+1)
        else:
            print('Entered runs not available on score card')
    elif ch==6:
        x=int(input('Enter the runs to be checked'))
        if x in t:
            print('No of times',x,'runs in an over:',t.count(x))
        else:
            print('Entered runs not available on score card')
    elif ch==7:
        print('Thank you')
    else:
        print('Enter a number from 1-7')
        
            
        
