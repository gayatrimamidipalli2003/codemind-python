n=int(input())
a=list(map(int,input().split()))
r=[]
sum=0
for i in range(n):
    if a[i] not in r:
        r.append(a[i])
for i in r:
    sum+=i
print(sum)