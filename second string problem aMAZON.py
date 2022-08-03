n=input("enter a string")
s=[]
c=0
x=0
flag=0

while x<len(n):
    if(n[x] in '1234567890'):
        s+=[c]
    c+=1
    x+=1

while(len(s)>=2):
    count=0
    str2=n[s[0]:s[1]+1]
    for i in s2:
        if(i.isalnum()==False):
            count+=1
    if count==3:
        y=int(n[num1])
        z=int(n[num2])
        print(bool(y+z==10),',',end='')
        print('(',y,'+',z,')')
        flag+=1
    del s[0]
if flag==0:
    print("False, no two numbers can be added from input")
        
    
    
    
        

        
        
