n=int(input())
for i in range(2,int(n**0.5)):
    if n%i==0:
        print('Not Mega Prime')
        break
else:
    c=d=0
    while n:
        r=n%10
        c+=1
        n//=10
        if r==2 or r==3 or r==5 or r==7:
            d+=1
if c==d:
    print('Mega Prime')
else:
    print('Not Mega Prime')