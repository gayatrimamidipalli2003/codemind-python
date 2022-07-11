n=int(input())
s=str(n)
l=len(s)
a=b=c=0
while n:
    rem=n%10
    if rem%2==0:
        a+=1
    elif rem%2!=0:
        b+=1
    else:
        c+=1
    n//=10
if a==l:
    print('Even')
elif b==l:
    print('Odd')
else:
    print('Mixed')