s=input()
s=s.lower()
s=s.split()
v='aeiou'
r=[]
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
print(min(r))