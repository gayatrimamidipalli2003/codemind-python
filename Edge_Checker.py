a,b=map(int,input().split())
if a+1==b or (a==10 and b==1):
    print('Yes')
elif b+1==a or (a==1 and b==10):
    print('Yes')
else:
    print('No')
    