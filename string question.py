n=input("enter an input")
x=''
s1=[]
s2=[]
for i in n:
    if (i.isupper()==True):
        s1+=[i]
        s1.sort()
    elif (i.islower()==True):
        s2+=[i]
        s2.sort()
while (s1!=[] and s2!=[]):
    x+=s1[0]
    del(s1[0])
    x+=s2[0]
    del(s2[0])
print(x)
        
