n=int(input("enter a decimal number"))
d=n
L=[]
while(d!=0):
    rem=d%2
    L+=[rem]
    d=d//2
print("binary value is",end=' ')
x=len(L)-1
for i in range(x,-1,-1):
    print(L[i],end=" ")

d=n
L=[]
while(d!=0):
    rem=d%8
    L+=[rem]
    d=d//8
print("\nOctal value:",end='')
x=len(L)-1
for i in range(x,-1,-1):
    print(L[i],end=" ")

d=n
L=[]
while(d!=0):
    rem=d%16
    L+=[rem]
    d=d//16
print("\nHexadecimal Value",end='')
x=len(L)-1
for i in range(x,-1,-1):
    if(L[i]==10):
        print('A',end='')
    elif(L[i]==11):
        print('B',end='')
    elif(L[i]==12):
        print('C',end='')
    elif(L[i]==13):
        print('D',end='')
    elif(L[i]==14):
        print('E',end='')
    elif(L[i]==15):
        print('F',end='')
    else:
        print(L[i],end='')
