n=int(input())
x=0
while n:
    rem=n%10
    if rem>x:
        x=rem
    n//=10
print(x)
    