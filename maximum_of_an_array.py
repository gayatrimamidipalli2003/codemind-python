n=int(input())
a=list(map(int,input().split()))
max=a[0]
for i in range(0,n):
    if max<a[i]:
        max=a[i]
print(max)