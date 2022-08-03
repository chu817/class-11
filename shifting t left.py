L=[2,4,1,7,8,9,6]
n=len(L)
print(L)
k=L[0]
for i in range(0,n-1):
       L[i]=L[i+1]
L[n-1]=k
print(L)    
