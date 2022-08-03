l=eval(input('enter a list:'))
print(l)
n=len(l)
print('delete an element')
x=int(input("Enter element to be deleted"))
for i in range(n):
    if(l[i]==x):
        del l[i]
        print(x,"element is deleted")
        break
else:
    print("element is not in the list")
