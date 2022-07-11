s=input()
c=1
count=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        if count<c:
            count=c
        c=1
if count<c:
    count=c
print(count)
        
    