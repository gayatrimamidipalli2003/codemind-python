s=input()
s=s.split()
r=[]
for i in s:
    c=0
    for j in i:
        c+=1
    r.append(c)
print(*r)