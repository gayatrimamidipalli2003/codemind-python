n=int(input())
a=list(map(int,input().split()))
c=0
r=[]
for i in a:
    i=str(i)
    le=len(i)
    r.append(le)
d=0
for i in r:
    if i==min(r):
        d+=1
print(d)