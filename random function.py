import random
n=random.randrange(1,4)
x=random.randint(1,n)
print(x,n)
for i in range(x,n+1):
    print(i,end='#')
