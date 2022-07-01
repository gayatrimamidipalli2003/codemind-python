n=int(input())
rev=revv=0
sq=n**2
while n:
    rem=n%10
    rev=rev*10+rem
    n//=10
sor=rev**2
while sor:
    rem=sor%10
    revv=revv*10+rem
    sor//=10
if sq==revv:
    print(True)
else:
    print(False)
