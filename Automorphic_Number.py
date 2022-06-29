n=int(input())
sq=n**2
temp=n
d=0
n1=n2=0
while temp:
    rem=temp%10
    n1=n1*10+rem
    temp//=10
while n:
    d+=1
    n//=10
while d:
    rem=sq%10
    n2=n2*10+rem
    sq//=10
    d-=1
if n1==n2:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')