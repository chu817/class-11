a=int(input('a'))
b=int(input('b'))
c=int(input('c'))

if(a>b>c or c>b>a):
    print(b)
elif(c>a>b or b>a>c):
    print(a)
else:
    print(c)
