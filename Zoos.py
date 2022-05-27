a=input()
c=0
d=0
for i in a:
    if i=='z':
        c+=1
    else:
        d+=1
if 2*c==d:
    print('Yes')
else:
    print('No')