a=input()
b=input()
a=a.split()
b=b.split()
r=[]
for i in a:
    for j in b:
        if i==j:
            if a.count(i)==1 and b.count(j)==1:
                r.append(i)
print(len(r))