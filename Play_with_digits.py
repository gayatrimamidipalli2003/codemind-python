def ds(n):
    s=0
    while n:
        rem=n%10
        s+=rem
        n//=10
    return s
n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum+=ds(i)
print(sum)
    