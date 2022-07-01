s=input()
v=list('aeiou')
s=s.split()
for i in s:
    for j in i:
        if j in v:
            v.remove(j)
if len(v)==0:
    print(0)
else:
    print(*v)
        