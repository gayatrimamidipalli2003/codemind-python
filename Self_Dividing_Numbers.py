a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    c=0
    d=0
    while temp%10!=0:
        rem=temp%10
        temp//=10
        if i%rem==0:
            c+=1
        d+=1
    if c==d and i%10!=0:
        print(i,end=' ')
   
