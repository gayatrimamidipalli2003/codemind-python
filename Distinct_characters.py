a=input().lower()
a=a.replace(' ','')
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
b=sorted(b)
b=str(b)
b=b.replace('[','')
b=b.replace(']','')
b=b.replace(' ','')
b=b.replace(',','')
b=b.replace("'","")
print(b)