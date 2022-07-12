n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
r=[]
for i in a:
    if i<x or i>y:
        r.append(i)
        c=1
if c==0:
    print('-1')
else:
    print(min(r))