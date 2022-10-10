s=input().lower()
v='aeiou'
c='bcdfghjklmnpqrstvwxyz'
l=[]
s=s.split()
for i in s:
    for j in v:
        if i not in l:
            if i.startswith(j):
                l.append(i)
print(len(l))