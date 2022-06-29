def pali(n):
    rev=0
    temp=n
    while temp:
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    if rev==n:
        return 1
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if pali(i):
        c+=1
print(c)