n=int(input())
rev=0
temp=n
while n:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)