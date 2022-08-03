string="PytHoN 3.7"
s2=''
for i in string:
    if(i.islower()):
        s2+='$'
    elif(i.isupper()):
        s2+=chr(ord(i.lower())+2)
    elif(i.isdigit()):
        s2+='#'
    else:
        s2+='%'
for i in range(len(s2)-1,-1,-1):
    print(s2[i],end='')
