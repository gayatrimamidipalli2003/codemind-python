n=int(input())
a=[]
b=[]
for i in range(2):
    for j in range(n):
        m=list(map(int,input().split()))
        if i==0:
            for h in m:
                a.append(h)
        if i==1:
            for g in m:
                b.append(g)
for k in range(n*n):
    if k%n==(n-1):
        print(a[k]+b[k])
    else:
        print(a[k]+b[k],end=' ')