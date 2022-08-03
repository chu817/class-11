n=input("enter a line")
n2=''
for i in n:
    if (i in "aeiouAEIOU"):
        n2+='@'
    elif(i in "1234567890"):
        n2+='*'
    elif(i==' '):
        n2+='!'
    elif(i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
        n2+=i
    else:
        n2+='X'
print(n2)
        
