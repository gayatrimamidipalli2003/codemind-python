a=input()
l=len(a)
min=1000000
c=0
for i in range(0,l):
    if a[i]==" ":
        if min>c:
            min=c
        c=0
    else:
        c+=1
if c<min:
    print(c)
else:
    print(min)