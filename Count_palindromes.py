def pali(n):
    rev=0
    temp=n
    while n:
        rem=n%10
        rev=rev*10+rem
        n//=10
    if rev==temp:
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if pali(i):
        c+=1
print(c)
    