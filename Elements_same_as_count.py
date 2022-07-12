n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    co=a.count(a[i])
    if a[i]==co:
        c+=1
        print(a[i],end=' ')
        a[i]=0
if c==0:
    print('-1')