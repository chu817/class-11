L=eval(input("enter a list to count the number of times each element is repeated"))
M=()
N=()
for i in L:
    if i not in M:
        x=0
        for j in L:
            if(i==j):
                x+=1
        M+=(i,)
        N+=((i,x),)
print(N)
        
