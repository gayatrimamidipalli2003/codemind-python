import math
n=int(input())
temp=n
s=0
le=int(math.log10(n))+1
while n:
    rem=n%10
    s=s+rem**le
    n//=10
    le-=1
if s==temp:
    print(True)
else:
    print(False)
    