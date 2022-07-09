n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i>=0:
        i=str(i)
        le=len(i)
        if le==k:
            c+=1
    else:
        i=str(i)
        le=len(i)
        if (le-1)==k:
            c+=1
print(c)