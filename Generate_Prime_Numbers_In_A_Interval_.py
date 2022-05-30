a=int(input())
b=int(input())
while a<=b:
    x=1
    c=0
    while x<=a//2:
        if a%x==0:
            c+=1
        x+=1
    if c==1:
        print(a)
    a+=1