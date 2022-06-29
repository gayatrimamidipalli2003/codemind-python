n=int(input())
a=list(map(int,input().split()))
arr=0
for i in range(0,n):
    arr+=a[i]
print(arr)