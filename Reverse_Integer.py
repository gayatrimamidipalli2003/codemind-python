n=int(input())
rev=0
if n>0:
    while n:
        rem=n%10
        rev=rev*10+rem
        n//=10
    print(rev)
else:
    n*=-1
    while n:
        rem=n%10
        rev=rev*10+rem
        n//=10
    print('-',end='')
    print(rev)
    