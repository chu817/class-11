s=input("enter a string")
while len(s)<=4:
    if(s[-1]=='z'):
        s=s[0:3]+'$'
    elif 'a' in s:
        s=s[0]+'&@'
    elif not int(s[0]):
        s='!'+s[1:]+'%'
    else:
        s+='#'
print(s)
        
