import math
n=int(input())
s=0
temp=n
le=int(math.log10(n)+1)
while n:
    rem=n%10
    s+=rem**le
    le-=1
    n//=10
if s==temp:
    print(True)
else:
    print(False)