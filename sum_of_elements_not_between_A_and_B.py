n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in range(0,n):
    if arr[i]<a or arr[i]>b:
        sum+=arr[i]
print(sum)

