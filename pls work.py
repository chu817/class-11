n=input("enter a string line")
s=''
j=0
k=-1
for i in n:
    s+=i
    if(i==' '):
        s=s.replace(' ','')
        for l in s:
            if(s[k]==s[j]):
                j+=1
                k-=1
                continue
            else:
                s=''
                break
            print(s)
            s=''
            break
        
