n=int(input())
a=list(map(int,input().split()))
se=0
so=0
for i in range(0,n):
    if a[i]%2==0:
        se+=a[i]
    else:
        so+=a[i]
if se>so:
    print(se-so)
else:
    print(so-se)
