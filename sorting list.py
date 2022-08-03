L=[2,4,1,7,8,9,6]
print(L)
n=len(L)
for i in range(n-1):
    for j in range(i+1,n):
        if(L[j]>L[i]):
            L[i],L[j]=L[j],L[i]
print(L)
            
