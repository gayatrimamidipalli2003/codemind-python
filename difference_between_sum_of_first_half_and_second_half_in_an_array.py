n=int(input())
a=list(map(int,input().split()))
sum1=sum2=0
for i in range(0,(n//2)):
    sum1+=a[i]
for i in range((n//2),n):
    sum2+=a[i]
if sum1>sum2:
    print(sum1-sum2)
else:
    print(sum2-sum1)