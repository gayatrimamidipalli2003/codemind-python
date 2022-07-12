n=int(input())
a=list(map(int,input().split()))
c=0
r=[]
for i in range(n):
    if a[i] not in r:
        r.append(a[i])
for i in r:
    if i%2==0:
        c+=1
print(c)