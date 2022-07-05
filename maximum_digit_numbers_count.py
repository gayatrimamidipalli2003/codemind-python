n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    i=str(i)
    le=len(i)
    c=max(le,c)
for i in a:
    i=str(i)
    le=len(i)
    if le==c:
        print(i,end=' ')
    
    
    