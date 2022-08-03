a,b,c,d,e,f,g,h,i=int(input('a')),int(input('b')),int(input('c')),int(input('d')),int(input('e')),int(input('f')),int(input('g')),int(input('h')),int(input('i'))
L={a,b,c,d,e,f,g,h,i}
m=0
for x in L:
   if(x>m):
       m=x
print(m,"is the greatest")
