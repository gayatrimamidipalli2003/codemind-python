s=input()
s=s.lower()
s=s.split()
v='aeiou'
r=[]
c1=0
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
for i in r:
    if i==max(r):
        c1+=1
print(c1)