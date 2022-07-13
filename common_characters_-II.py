a=input().lower()
b=input().lower()
c=''
for i in a:
    if i in b and i not in c:
        c+=i
for i in b:
    if i in a and i not in c:
        c+=i
c=sorted(c)
c=str(c)
c=c.replace('[','')
c=c.replace(']','')
c=c.replace(' ','')
c=c.replace(',','')
c=c.replace("'",'')
print(len(c))