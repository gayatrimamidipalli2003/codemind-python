n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i>=0:
        i=str(i)
        le=len(i)
        print(le,end=' ')
    else:
        i=str(i)
        le=len(i)
        print(le-1,end=' ')
    