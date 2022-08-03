s=input("enter a string")
s2=''
for i in s:
    if(i in 'AEIOUaeiou'):
        s2+='*'
    else:
        s2+=i
print('Output:',s2)
