n=input()
n=n.lower()
n=n.split()
v='aeiou'
r=[]
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
d=0
for i in r:
    if i==max(r):
        d+=1
print(d)
    