n=int(input())
a=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(n):
    if a[i]<=k:
        sum+=a[i]
print(sum)