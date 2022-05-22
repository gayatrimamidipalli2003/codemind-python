n=int(input())
s=0
p=1
while n:
    rem=n%10
    s+=rem
    p*=rem
    n//=10
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')
    