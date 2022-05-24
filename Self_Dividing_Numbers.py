def sd(n):
    c=0
    d=0
    temp=n
    while n:
        rem=n%10
        c+=1
        if rem!=0 and temp%rem==0:
            d+=1
        n//=10
    if c==d:
        print(temp,end=' ')
a=int(input())
b=int(input())
for i in range(a,b+1):
    sd(i)
            
            
    