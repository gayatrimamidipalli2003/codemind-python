n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
k = int(input())
count = 0
for i in range(0,n):
    if a[i]<=k and b[i]>=k:
        count+=1
print(count)