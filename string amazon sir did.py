s=input("enter the string")
count=0
x=0
print('s:',s)
for i in range(len(s)):
    if(s[i].isdigit() and count==0):
        x=int(s[i])
        print(x)
    elif(x!=0 and not(s[i].isalnum())):
        count+=1
        print('count',count)
    if(count>3):
        count=0
        x=0
    elif(s[i].isdigit() and count==3):
        y=int(s[i])
        if(x+y==10):
            print('True')
            break
        x=y
        y=0
        count=0
else:
    print('False')

