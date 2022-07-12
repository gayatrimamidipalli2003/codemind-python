n=int(input())
a=list(map(int,input().split()))
sett=set(a)
r=[]
c=0
for i in sett:
    if i==a.count(i):
        r.append(i)
        c=1
if c==0:
    print('-1')
else:
    print(min(r),max(r))