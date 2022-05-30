n=int(input())
a=list(map(int,input().split()))
x=0
for i in range(0,n):
    if a[i]%2!=0:
        x=a[i]
print(x)
