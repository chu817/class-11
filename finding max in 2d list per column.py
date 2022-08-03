r1=int(input("enter the number of rows"))
c1=int(input("enter the number of columns"))
L=[[0 for j in range(c1)]for i in range(r1)]
for i in range(r1):
    for j in range(c1):
        print('L[',i,'][',j,']=',end='')
        L[i][j]=int(input())
print()
for i in range(r1):
    for j in range(c1):
        print(L[i][j],end='')
    print()

for i in range(c1):
    m=0
    for j in range(r1):
        if(L[j][i]>m):
            m=L[j][i]
    print(m,"is the max value")

            
    

                
    

        
