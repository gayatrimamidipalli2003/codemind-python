n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    pro=1
    for j in range(0,n):
        if i!=j:
            pro*=a[j]
    print(pro,end=' ')