def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
c=0
max=max(a)
min=min(a)
maxi=a.index(max)
mini=a.index(min)
if mini>maxi:
    for i in range(maxi,mini+1):
        if prime(a[i]):
            c+=1
    print(c)
else:
    for i in range(mini,maxi+1):
        if prime(a[i]):
            c+=1
    print(c)
        