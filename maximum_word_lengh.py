n = input()
c=0
max=0
for i in range(0,len(n)):
    if n[i]==' ':
        if max<c:
            max=c
        c=0
    else:
        c+=1
if c>max:
    max=c
print(max)