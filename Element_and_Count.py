n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n):
    if a[i] not in s:
        s.append(a[i])
for i in s:
    print(i,a.count(i),end=' ')
        