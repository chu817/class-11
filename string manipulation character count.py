s=input("enter a string:")
c=input("enter a char to be counted:")
count=0
for i in s:
    if(i==c):
        count+=1
print('The character',c,'is present',count,'times in the string')
