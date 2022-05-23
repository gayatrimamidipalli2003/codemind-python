x=int(input())
temp=x
s=0
while temp:
    r=temp%10
    temp//=10
    fact=1
    for i in range(r,0,-1):
        fact*=i
    s+=fact
if s==x:
    print('The number',x,'is a strong number')
else:
    print('The number',x,'is not a strong number')
    