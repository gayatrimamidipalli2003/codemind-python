s=input()
c=0
i=0
l=len(s)
count=0
while l:
    if s[i]=='R':
        c+=1
    else:
        c-=1
    i+=1
    if c==0:
        count+=1
    l-=1
print(count)