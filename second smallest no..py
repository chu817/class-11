a,b,c=int(input('A')),int(input('b')),int(input('c'))

if(a>b and a>c):
    if(b>c):
        print(b,"is the second smallest")
    else:
        print(c,"is the second smallest number")
elif(b>c and b>a):
    if(c>a):
        print(c,"is the second smallest")
    else:
        print(a,"is the second smallest")
elif(c>b and c>a):
    if(a>b):
        print(a,"is the second smallest")
    else:
        print(b,"is the second smallest number")
