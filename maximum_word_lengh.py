a=input()
l=len(a)
c=0
m=0
for i in range(0,l):
    if a[i]==' ':
        if m<c:
            m=c
        c=0
    else:
        c+=1
if c>m:
    print(c)
else:
    print(m)