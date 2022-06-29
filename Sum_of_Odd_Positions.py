n=int(input())
a=list(map(int,input().split()))
o=0
for i in range(o,n):
    if i%2!=0:
        o+=a[i]
print(o)