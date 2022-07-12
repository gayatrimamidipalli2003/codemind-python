n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
r=[]
c=0
for i in a:
    if i>=x and i<=y:
        r.append(i)
        c=1
if c==0:
    print('-1')
else:
    print(min(r))