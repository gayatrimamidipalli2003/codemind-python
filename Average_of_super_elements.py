n=int(input())
a=list(map(int,input().split()))
sett=set(a)
sum=c=0
for i in sett:
    if i==a.count(i):
        sum+=i
        c+=1
if c==0:
    print('-1')
else:
    res=sum/c
    print('%.2f'%res)