a=int(input())
b=int(input())
x=1
sum=0
while x<=(a//2):
    if a%x==0:
        sum+=x
    x+=1
y=1
if sum==b:
    sum=0
    while y<=(b//2):
        if b%y==0:
            sum+=y
        y+=1
    if sum==a:
        print('Amicable')
else:
    print('Not Amicable')
    
