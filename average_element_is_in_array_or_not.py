n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,n):
    sum+=a[i]
res=sum//n
for i in a:
    if i==res:
        print(True)
        break
else:
    print(False)