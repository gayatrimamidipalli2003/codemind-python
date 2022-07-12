n=int(input())
a=list(map(int,input().split()))
c=0
sett=set(a)
for i in sett:
    if i==a.count(i):
        c+=1
print(c)