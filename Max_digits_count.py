n=int(input())
a=list(map(int,input().split()))
c=0
r=[]
for i in a:
    i=str(i)
    le=len(i)
    r.append(le)
for i in r:
    if i==max(r):
        c+=1
print(c)