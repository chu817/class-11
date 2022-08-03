s=input("enter a string")
i=0
j=len(s)-1
while(i<=j):
    if(s[i]!=s[j]):
        print(s,"is not a palindrome")
        break
    i+=1
    j-=1
else:
    print(s,"is a palindrome")
