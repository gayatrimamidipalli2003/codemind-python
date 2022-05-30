n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    min=a[0]
    if a[i]<min:
        min=a[i]
print(min)