def pali(n):
    rev=0
    temp=n
    while n:
        rem=n%10
        rev=rev*10+rem
        n//=10
    if rev==temp:
        return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if pali(i):
        print(i,end=' ')
    