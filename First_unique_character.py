a=input().lower()
a=a.replace(' ','')
s=[]
c=0
for i in a:
    if a.count(i)==1:
        s.append(i)
        c=1
if c==0:
    print('-1')
else:
    for i in s:
        print(i)
        break