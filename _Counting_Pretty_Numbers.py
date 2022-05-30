n=int(input())
while n:
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        rem=i%10
        if rem==2 or rem==3 or rem==9:
            c+=1
    print(c)
    n-=1