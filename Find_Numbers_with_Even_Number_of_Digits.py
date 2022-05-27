n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(0,n):
    d=0
    while a[i]:
        rem=a[i]%10
        d+=1
        a[i]//=10
    if d%2==0:
        count+=1
print(count)
        
    