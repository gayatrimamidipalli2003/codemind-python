n=int(input())
a=list(map(int,input().split()))
r=[]
c=0
for i in a:
    i=str(i)
    le=len(i)
    r.append(le)
for i in r:
    if i==min(r):
        c+=1
print(c)