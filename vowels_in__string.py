s=input()
v='aeiouAEIOU'
r=[]
for i in s:
    if i in v:
        if i not in r:
            r.append(i)
if len(r)==0:
    print(-1)
else:
    print(*r)