x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
r=[]
for i in a:
    if i not in b:
        r.append(i)
for i in b:
    if i not in a:
        r.append(i)
print(*r)
        