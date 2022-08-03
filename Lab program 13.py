n=int(input("enter the number of values for the list"))
L=[]
for i in range(n):
    print('Enter L[',i,']:')
    L+=[int(input())]
print('The Original List',L)
L2,L3=list(L),list(L)
ch=0
while(ch!=5):
    print('\n1.Max \n2.Min \n3.Sort-Asc(Selection) \n4.Sort-Desc(Bubble)\n5.Exit')
    ch=int(input("enter your choice"))
    if(ch==1):
        mx=L[0]
        for i in range(1,n):
            if(mx<L[i]):
                mx=L[i]
        print('Max Element in the list is:',mx)
    elif(ch==2):
        mn=L[0]
        for i in range(1,n):
            if(mn>L[i]):
                mn=L[i]
        print('Min element in the list is:',mn)

    elif(ch==3):
        for i in range(n):
            t=i
            for j in range(i+1,n):
                if(L2[t]>L2[j]):
                    t=j
            L2[i],L2[t]=L2[t],L2[i]
        print('Sort asc:',L2)
    elif(ch==4):
        for i in range(n):
            for j in range(0,n-1):
                if(L3[j]<L3[j+1]):
                    L3[j],L3[j+1]=L3[j+1],L3[j]
        print('Sort desc:',L3)
    elif(ch==5):
        print('Thank You!!!')
