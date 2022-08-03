'''length of a digit'''
t=(4532,231,7321,456,12)
for i in t:
    j=i
    c=0
    while(j!=0):
        c+=1
        j=j//10
    if(c==3):
        print(i,end=' ')
    

   
