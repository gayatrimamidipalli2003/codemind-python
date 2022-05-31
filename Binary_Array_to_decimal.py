n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,n):
    sum+=a[i]*(2**(n-1))
    n-=1
print(sum)